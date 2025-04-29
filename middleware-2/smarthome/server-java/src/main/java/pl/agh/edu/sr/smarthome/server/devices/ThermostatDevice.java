package pl.agh.edu.sr.smarthome.server.devices;

import pl.agh.edu.sr.smarthome.generated.DeviceIdentity;
import pl.agh.edu.sr.smarthome.generated.DeviceInfo;
import pl.agh.edu.sr.smarthome.generated.DeviceType;
import pl.agh.edu.sr.smarthome.generated.PowerState;
import pl.agh.edu.sr.smarthome.generated.ThermostatMode;
import pl.agh.edu.sr.smarthome.generated.ThermostatState;

public class ThermostatDevice implements SmartDevice {
    private final DeviceIdentity identity;
    private final String name;
    private PowerState powerState;
    private float targetTemperatureCelsius;
    private float currentTemperatureCelsius;
    private ThermostatMode mode;

    public ThermostatDevice(DeviceIdentity identity, String name) {
        this.identity = identity;
        this.name = name;
        this.powerState = PowerState.OFF;
        this.targetTemperatureCelsius = 25.0f;
        this.currentTemperatureCelsius = 25.0f;
        this.mode = ThermostatMode.HEAT;
    }

    public synchronized ThermostatState getState() {
        return ThermostatState.newBuilder()
                .setPowerState(this.powerState)
                .setTargetTemperatureCelsius(this.targetTemperatureCelsius)
                .setCurrentTemperatureCelsius(this.currentTemperatureCelsius)
                .setMode(this.mode)
                .build();
    }

    public DeviceIdentity getIdentity() { return this.identity; }

    public synchronized void setPowerState(PowerState state) { 
        this.powerState = state; 
    }

    public synchronized void setTargetTemperature(float temperature) {
        this.targetTemperatureCelsius = temperature;
    }

    public synchronized void setCurrentTemperature(float temperature) {
        this.currentTemperatureCelsius = temperature;
    }

    public synchronized void setMode(ThermostatMode mode) {
        this.mode = mode;
    }

    @Override
    public DeviceInfo getDeviceInfo(String serverLocation) {
        return DeviceInfo.newBuilder()
                .setIdentity(this.identity)
                .setType(DeviceType.THERMOSTAT)
                .setName(this.name)
                .setServerLocation(serverLocation)
                .build();
    }
}
