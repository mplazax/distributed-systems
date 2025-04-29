package pl.agh.edu.sr.smarthome.server.devices;

import pl.agh.edu.sr.smarthome.generated.DeviceIdentity;
import pl.agh.edu.sr.smarthome.generated.DeviceInfo;
import pl.agh.edu.sr.smarthome.generated.DeviceType;
import pl.agh.edu.sr.smarthome.generated.LightState;
import pl.agh.edu.sr.smarthome.generated.PowerState;


public class LightDevice implements SmartDevice {
    private final DeviceIdentity identity;
    private final String name;
    private PowerState powerState;
    private int brightnessPercentage;

    public LightDevice(DeviceIdentity identity, String name) {
        this.identity = identity;
        this.name = name;
        this.powerState = PowerState.OFF;
        this.brightnessPercentage = 0;
    }

    public DeviceIdentity getIdentity() { return this.identity; }

    public synchronized LightState getState() {
        return LightState.newBuilder()
                .setPowerState(this.powerState)
                .setBrightnessPercentage(this.brightnessPercentage)
                .build();
    }

    public synchronized void setPowerState(PowerState state) { 
        this.powerState = state; 
    }

    public synchronized void setBrightness(int brightness) {
        if (brightness < 0 || brightness > 100) {
            throw new IllegalArgumentException("Brightness must be between 0 and 100");
        }
        this.brightnessPercentage = brightness;
    }

    @Override
    public DeviceInfo getDeviceInfo(String serverLocation) {
        return DeviceInfo.newBuilder()
                .setIdentity(this.identity)
                .setType(DeviceType.LIGHT)
                .setName(this.name)
                .setServerLocation(serverLocation)
                .build();
    }
}
