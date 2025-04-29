package pl.agh.edu.sr.smarthome.server;

import pl.agh.edu.sr.smarthome.generated.DeviceInfo;
import pl.agh.edu.sr.smarthome.generated.DeviceIdentity;
import pl.agh.edu.sr.smarthome.server.devices.SmartDevice;
import pl.agh.edu.sr.smarthome.server.devices.*;

import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;
import java.util.stream.Collectors;

public class DeviceRepository {

    private final Map<String, SmartDevice> devices = new ConcurrentHashMap<>();

    private final String serverLocation;


    public DeviceRepository(String serverLocation) {
        if (serverLocation == null || serverLocation.trim().isEmpty()) {
            throw new IllegalArgumentException("Server location cannot be null or empty");
        }
        this.serverLocation = serverLocation;
        System.out.println("DeviceRepository initialized for server at: " + serverLocation);
    }

    public void addDevice(SmartDevice device) {
        if (device == null || device.getIdentity() == null || device.getIdentity().getId() == null) {
            System.err.println("Attempted to add invalid device or device with null ID.");
            return; // lub rzuć wyjątek
        }
        String deviceId = device.getIdentity().getId();
        devices.put(deviceId, device);
        System.out.println("Device added/updated: ID=" + deviceId + ", Type=" + device.getClass().getSimpleName());
    }

    public Optional<SmartDevice> findDevice(String id) {
        return Optional.ofNullable(devices.get(id));
    }

    public List<DeviceInfo> getAllDeviceInfo() {
        return devices.values().stream()
                .map(device -> device.getDeviceInfo(this.serverLocation)) // Przekazujemy lokalizację serwera
                .collect(Collectors.toList());
    }

    // --- Metody pomocnicze do znajdowania konkretnych typów urządzeń ---
    // Ułatwiają kod w implementacjach usług gRPC, unikając rzutowania i sprawdzania typów.

    public Optional<LightDevice> findLight(String id) {
        return findDevice(id)
                .filter(LightDevice.class::isInstance) // Sprawdź, czy to instancja LightDevice
                .map(LightDevice.class::cast);         // Rzutuj na LightDevice
    }


    public Optional<ThermostatDevice> findThermostat(String id) {
        return findDevice(id)
                .filter(ThermostatDevice.class::isInstance)
                .map(ThermostatDevice.class::cast);
    }


    public Optional<PTZCameraDevice> findCamera(String id) {
        return findDevice(id)
                .filter(device -> device instanceof PTZCameraDevice)
                .map(device -> (PTZCameraDevice) device);
    }


    public void initializeWithSampleDevices() {
        System.out.println("Initializing repository with sample devices...");

        // Create devices with the available constructors then set their states
        LightDevice livingLight = new LightDevice(
                DeviceIdentity.newBuilder().setId("living_light").build(),
                "Światło Salon");
        livingLight.setPowerState(pl.agh.edu.sr.smarthome.generated.PowerState.OFF);
        livingLight.setBrightness(50);
        addDevice(livingLight);

        ThermostatDevice bedroomThermo = new ThermostatDevice(
                DeviceIdentity.newBuilder().setId("bedroom_thermo").build(),
                "Termostat Sypialnia");
        bedroomThermo.setPowerState(pl.agh.edu.sr.smarthome.generated.PowerState.ON);
        bedroomThermo.setTargetTemperature(21.5f);
        bedroomThermo.setCurrentTemperature(20.0f);
        bedroomThermo.setMode(pl.agh.edu.sr.smarthome.generated.ThermostatMode.HEAT);
        addDevice(bedroomThermo);

        ThermostatDevice kitchenThermo = new ThermostatDevice(
                DeviceIdentity.newBuilder().setId("kitchen_thermo").build(),
                "Termostat Kuchnia");
        kitchenThermo.setPowerState(pl.agh.edu.sr.smarthome.generated.PowerState.OFF);
        kitchenThermo.setTargetTemperature(20.0f);
        kitchenThermo.setCurrentTemperature(22.0f);
        addDevice(kitchenThermo);

        addDevice(new PTZCameraDevice(
                DeviceIdentity.newBuilder().setId("garden_cam").build(),
                "Kamera Ogród"));   

        System.out.println("Sample devices initialized. Total devices: " + devices.size());
    }
}
