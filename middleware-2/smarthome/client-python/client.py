import sys
import grpc
import smarthome_pb2
import smarthome_pb2_grpc
from google.protobuf import empty_pb2
from google.protobuf.wrappers_pb2 import Int32Value
import readline
import os
import atexit


DEFAULT_SERVER_ADDRESSES = ["localhost:50051", "localhost:50052"]

# Słownik przechowujący informacje o urządzeniach (ID -> DeviceInfo)
# DeviceInfo zawiera m.in. server_location
all_devices = {}

# Słownik przechowujący kanały i stuby dla każdego serwera (adres -> {'channel': ..., 'stubs': {...}})
server_connections = {}

# --- Funkcje Pomocnicze ---

def connect_to_servers(addresses):
    """Nawiązuje połączenie gRPC z podanymi adresami serwerów."""
    print("Attempting to connect to servers...")
    for address in addresses:
        try:
            channel = grpc.insecure_channel(address)
            try:
                discovery_stub = smarthome_pb2_grpc.DeviceDiscoveryStub(channel)
                discovery_stub.ListDevices(empty_pb2.Empty(), timeout=2)
            except grpc.RpcError as e:
                 if e.code() == grpc.StatusCode.DEADLINE_EXCEEDED:
                    print(f"  Warning: Timeout connecting to {address}. Server might be down or slow.")
                 elif e.code() == grpc.StatusCode.UNAVAILABLE:
                    print(f"  Warning: Server at {address} is unavailable.")
                 else:
                    print(f"  Warning: Error connecting to {address}: {e.code()} - {e.details()}")
                 channel.close()
                 continue

            server_connections[address] = {
                'channel': channel,
                'stubs': {
                    'discovery': smarthome_pb2_grpc.DeviceDiscoveryStub(channel),
                    'light': smarthome_pb2_grpc.LightControlStub(channel),
                    'thermostat': smarthome_pb2_grpc.ThermostatControlStub(channel),
                    'camera': smarthome_pb2_grpc.CameraControlStub(channel),
                }
            }
            print(f"  Successfully connected to {address}")
        except Exception as e:
            print(f"  Failed to establish connection to {address}: {e}")

    if not server_connections:
        print("Error: Could not connect to any server. Exiting.")
        sys.exit(1)

def list_all_devices():
    """Pobiera listę urządzeń ze wszystkich połączonych serwerów."""
    global all_devices
    all_devices.clear()
    print("\nFetching devices from all connected servers...")
    for address, connection_data in server_connections.items():
        try:
            discovery_stub = connection_data['stubs']['discovery']
            response = discovery_stub.ListDevices(empty_pb2.Empty(), timeout=5)
            print(f"  Devices from {address}:")
            if not response.devices:
                 print("    (No devices reported by this server)")
                 continue

            for device_info in response.devices:
                if not device_info.server_location or device_info.server_location != address:
                     print(f"    Warning: Device {device_info.identity.id} from {address} has missing or incorrect server location ('{device_info.server_location}'). Skipping.")
                     continue

                subtype_str = f", Subtype: {smarthome_pb2.ThermostatSubtype.Name(device_info.thermostat_subtype)}" if device_info.HasField('thermostat_subtype') else ""
                print(f"    - ID: {device_info.identity.id:<15} | Name: {device_info.name:<25} | Type: {smarthome_pb2.DeviceType.Name(device_info.type):<12}{subtype_str}")
                all_devices[device_info.identity.id] = device_info # Zapisz info

        except grpc.RpcError as e:
            print(f"  Error listing devices from {address}: {e.code()} - {e.details()}")
        except Exception as e:
            print(f"  Unexpected error listing devices from {address}: {e}")
    print("-" * 70)


def get_device_stub_and_info(device_id):
    """Zwraca odpowiedni stub gRPC i DeviceInfo dla danego ID urządzenia."""
    if device_id not in all_devices:
        print(f"Error: Device ID '{device_id}' not found in the current list. Try 'list' first.")
        return None, None

    device_info = all_devices[device_id]
    server_location = device_info.server_location

    if server_location not in server_connections:
        print(f"Error: Cannot connect to server {server_location} for device '{device_id}'. Server might be down.")
        return None, None

    connection_data = server_connections[server_location]

    service_type_map = {
        smarthome_pb2.LIGHT: 'light',
        smarthome_pb2.THERMOSTAT: 'thermostat',
        smarthome_pb2.PTZ_CAMERA: 'camera',
    }

    service_key = service_type_map.get(device_info.type)

    if not service_key or service_key not in connection_data['stubs']:
        print(f"Error: No suitable gRPC service stub found for device type {smarthome_pb2.DeviceType.Name(device_info.type)} on server {server_location}.")
        return None, device_info # Zwracamy info, ale bez stuba

    return connection_data['stubs'][service_key], device_info


def print_device_status(device_id):
    """Pobiera i wyświetla status urządzenia."""
    stub, info = get_device_stub_and_info(device_id)
    if not stub: # Jeśli nie ma stuba (nawet jeśli info istnieje), nie możemy pobrać stanu
        return
    if not info: # Dodatkowe zabezpieczenie
        print(f"Error: Device info unexpectedly missing for ID '{device_id}'.")
        return

    identity = smarthome_pb2.DeviceIdentity(id=device_id)
    print(f"\nGetting status for {smarthome_pb2.DeviceType.Name(info.type)} '{device_id}' ({info.name}) from {info.server_location}...")

    try:
        if info.type == smarthome_pb2.LIGHT:
            state = stub.GetLightState(identity, timeout=5)
            print(f"  Status: Power = {smarthome_pb2.PowerState.Name(state.power_state)}, Brightness = {state.brightness_percentage}%")
        elif info.type == smarthome_pb2.THERMOSTAT:
            state = stub.GetThermostatState(identity, timeout=5)
            mode_str = f", Mode = {smarthome_pb2.ThermostatMode.Name(state.mode)}" if state.HasField('mode') else " (Mode N/A for Simple)"
            print(f"  Status: Power = {smarthome_pb2.PowerState.Name(state.power_state)}, Target = {state.target_temperature_celsius:.1f}°C, Current = {state.current_temperature_celsius:.1f}°C{mode_str}")
        elif info.type == smarthome_pb2.PTZ_CAMERA:
            state = stub.GetPTZCameraState(identity, timeout=5)
            print(f"  Status: Power = {smarthome_pb2.PowerState.Name(state.power_state)}, Pan = {state.pan_degrees}°, Tilt = {state.tilt_degrees}°, Zoom = {state.zoom_level}x")
        else:
            print(f"  Error: Status display not implemented for type {smarthome_pb2.DeviceType.Name(info.type)}")
    except grpc.RpcError as e:
        print(f"  Error getting status: {e.code()} - {e.details()}")
    except Exception as e:
        print(f"  Unexpected error getting status: {e}")


def set_device_state(device_id, property_name, value_str):
    """Ustawia stan właściwości urządzenia."""
    stub, info = get_device_stub_and_info(device_id)
    if not stub: return
    if not info: return

    identity = smarthome_pb2.DeviceIdentity(id=device_id)
    print(f"\nSetting {property_name} for {smarthome_pb2.DeviceType.Name(info.type)} '{device_id}' to '{value_str}' on {info.server_location}...")

    try:
        # --- Obsługa Światła ---
        if info.type == smarthome_pb2.LIGHT:
            if property_name == "power":
                p_state = smarthome_pb2.PowerState.Value(value_str.upper())
                req = smarthome_pb2.SetPowerRequest(identity=identity, desired_power_state=p_state)
                stub.SetPower(req, timeout=5)
                print(f"  Successfully set power to {value_str.upper()}.")
            elif property_name == "brightness":
                b_value = int(value_str)
                req = smarthome_pb2.SetBrightnessRequest(identity=identity, desired_brightness_percentage=b_value)
                stub.SetBrightness(req, timeout=5)
                print(f"  Successfully set brightness to {b_value}%.")
            else:
                print(f"  Error: Unknown property '{property_name}' for LIGHT.")
                return

        # --- Obsługa Termostatu ---
        elif info.type == smarthome_pb2.THERMOSTAT:
            if property_name == "power":
                p_state = smarthome_pb2.PowerState.Value(value_str.upper())
                req = smarthome_pb2.SetPowerRequest(identity=identity, desired_power_state=p_state)
                stub.SetPower(req, timeout=5)
                print(f"  Successfully set power to {value_str.upper()}.")
            elif property_name == "temp":
                t_value = float(value_str)
                req = smarthome_pb2.SetTemperatureRequest(identity=identity, desired_target_temperature_celsius=t_value)
                stub.SetTargetTemperature(req, timeout=5)
                print(f"  Successfully set target temperature to {t_value:.1f}°C.")
            elif property_name == "mode":
                m_value = smarthome_pb2.ThermostatMode.Value(value_str.upper())
                req = smarthome_pb2.SetModeRequest(identity=identity, desired_mode=m_value)
                try:
                    stub.SetMode(req, timeout=5)
                    print(f"  Successfully requested mode change to {value_str.upper()}.")
                    print("    (Note: Server will reject if thermostat is SIMPLE type)")
                except grpc.RpcError as e_mode:
                    if e_mode.code() == grpc.StatusCode.FAILED_PRECONDITION or e_mode.code() == grpc.StatusCode.UNIMPLEMENTED:
                        print(f"  Warning: Could not set mode. {e_mode.details()} (Likely a SIMPLE thermostat)")
                    else:
                        raise e_mode
            else:
                print(f"  Error: Unknown property '{property_name}' for THERMOSTAT.")
                return

        elif info.type == smarthome_pb2.PTZ_CAMERA:
            if property_name == "power":
                p_state = smarthome_pb2.PowerState.Value(value_str.upper())
                req = smarthome_pb2.SetPowerRequest(identity=identity, desired_power_state=p_state)
                stub.SetPower(req, timeout=5)
                print(f"  Successfully set power to {value_str.upper()}.")
            elif property_name in ["pan", "tilt", "zoom"]:
                try:
                    val = int(value_str)
                    ptz_req_args = {'identity': identity}
                    if property_name == "pan":
                        ptz_req_args['desired_pan_degrees'] = Int32Value(value=val)
                    elif property_name == "tilt":
                        ptz_req_args['desired_tilt_degrees'] = Int32Value(value=val)
                    elif property_name == "zoom":
                        ptz_req_args['desired_zoom_level'] = Int32Value(value=val)

                    ptz_req = smarthome_pb2.SetPTZRequest(**ptz_req_args)
                    stub.SetPTZ(ptz_req, timeout=5)
                    print(f"  Successfully set {property_name} to {val}.")

                except ValueError:
                    print(f"  Error: Invalid integer value '{value_str}' for {property_name}.")
                    return
            else:
                 print(f"  Error: Unknown property '{property_name}' for PTZ_CAMERA.")
                 return

        else:
            print(f"  Error: Setting state not implemented for type {smarthome_pb2.DeviceType.Name(info.type)}")

    except grpc.RpcError as e:
        print(f"  Error setting state: {e.code()} - {e.details()}")
    except ValueError as e:
        print(f"  Error: Invalid value format - {e}")
    except Exception as e:
        print(f"  Unexpected error setting state: {e}")


def print_help():
    """Wyświetla dostępne komendy."""
    print("\nAvailable commands:")
    print("  list          - Refresh and list all available devices from connected servers")
    print("  status <id>   - Show the current status of the device with the given ID")
    print("  set <id> <prop> <value> - Set a property of a device.")
    print("    Properties & Values:")
    print("      LIGHT:")
    print("        power [on|off]")
    print("        brightness [0-100]")
    print("      THERMOSTAT:")
    print("        power [on|off]")
    print("        temp [target_temp_float]")
    print("        mode [heat|cool|fan_only|auto] (Only for ADVANCED type)")
    print("      PTZ_CAMERA:")
    print("        power [on|off]")
    print("        pan [-180 to 180]")
    print("        tilt [-90 to 90]")
    print("        zoom [1-10] (or other range defined by server)")
    print("  help          - Show this help message")
    print("  exit          - Exit the client")
    print("-" * 70)


# --- Konfiguracja readline dla historii komend i uzupełniania ---
def setup_readline_history():
    """Konfiguruje readline do obsługi historii komend i uzupełniania."""
    histfile = os.path.join(os.path.expanduser("~"), ".smarthome_history")
    try:
        readline.read_history_file(histfile)
        readline.set_history_length(1000)
    except FileNotFoundError:
        pass
    
    atexit.register(readline.write_history_file, histfile)
    
    if 'libedit' in readline.__doc__:  # macOS
        readline.parse_and_bind("bind ^I rl_complete")
    else:  # Linux i inne
        readline.parse_and_bind("tab: complete")
    
    def completer(text, state):
        buffer = readline.get_line_buffer()
        parts = buffer.split()
        

        if not parts or (len(parts) == 1 and not buffer.endswith(' ')):
            commands = ["list", "status", "set", "help", "exit"]
            matches = [cmd for cmd in commands if cmd.startswith(text)]
        elif parts[0] in ['status', 'set'] and (len(parts) == 1 or (len(parts) == 2 and not buffer.endswith(' '))):
            matches = [dev_id + ' ' for dev_id in all_devices.keys() if dev_id.startswith(text)]
        elif parts[0] == 'set' and len(parts) >= 2 and parts[1] in all_devices and (len(parts) == 2 or (len(parts) == 3 and not buffer.endswith(' '))):
            device_type = all_devices[parts[1]].type
            
            if device_type == smarthome_pb2.LIGHT:
                properties = ["power", "brightness"]
            elif device_type == smarthome_pb2.THERMOSTAT:
                properties = ["power", "temp", "mode"]
            elif device_type == smarthome_pb2.PTZ_CAMERA:
                properties = ["power", "pan", "tilt", "zoom"]
            else:
                properties = []
            
            matches = [prop + ' ' for prop in properties if prop.startswith(text)]
        elif parts[0] == 'set' and len(parts) >= 3 and parts[1] in all_devices and (len(parts) == 3 or (len(parts) == 4 and not buffer.endswith(' '))):
            device_type = all_devices[parts[1]].type
            property_name = parts[2]
            
            if property_name == "power":
                values = ["on", "off"]
            elif property_name == "mode" and device_type == smarthome_pb2.THERMOSTAT:
                values = ["heat", "cool", "fan_only", "auto"]
            else:
                values = []
                
            matches = [val for val in values if val.startswith(text)]
        else:
            matches = []
            
        if state < len(matches):
            return matches[state]
        else:
            return None
    
    readline.set_completer(completer)
    
    if hasattr(readline, 'set_completer_delims'):
        readline.set_completer_delims(' \t\n;')

# --- główna pętla ---


if __name__ == '__main__':
    server_addresses = sys.argv[1:] if len(sys.argv) > 1 else DEFAULT_SERVER_ADDRESSES

    setup_readline_history()
    
    connect_to_servers(server_addresses)
    list_all_devices()
    print_help()

    try:
        while True:
            try:
                command_line = input("> ").strip()
                if not command_line: continue

                parts = command_line.split()
                action = parts[0].lower()

                if action == "exit":
                    break
                elif action == "list":
                    list_all_devices()
                elif action == "status" and len(parts) == 2:
                    device_id = parts[1]
                    print_device_status(device_id)
                elif action == "set" and len(parts) == 4:
                    device_id = parts[1]
                    prop = parts[2].lower()
                    value = parts[3]
                    set_device_state(device_id, prop, value)
                elif action == "help":
                    print_help()
                else:
                    print(f"Unknown command: '{command_line}'. Type 'help' for options.")

            except EOFError:
                print("\nExiting...")
                break
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"\nAn unexpected error occurred in the client loop: {e}")

    finally:
        print("\nClosing connections...")
        for address, connection_data in server_connections.items():
            try:
                connection_data['channel'].close()
                print(f"  Connection to {address} closed.")
            except Exception as e:
                print(f"  Error closing connection to {address}: {e}")