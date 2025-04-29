package pl.agh.edu.sr.smarthome.server.devices;

import pl.agh.edu.sr.smarthome.generated.DeviceIdentity;
import pl.agh.edu.sr.smarthome.generated.DeviceInfo;
import pl.agh.edu.sr.smarthome.generated.DeviceType;
import pl.agh.edu.sr.smarthome.generated.PowerState;
import pl.agh.edu.sr.smarthome.generated.PTZCameraState;

public class PTZCameraDevice implements SmartDevice {
    private final DeviceIdentity identity;
    private final String name;
    private PowerState powerState;
    private int zoom;
    private int pan;
    private int tilt;
    
    public PTZCameraDevice(DeviceIdentity identity, String name) {
        this.identity = identity;
        this.name = name;
        this.powerState = PowerState.OFF;
        this.zoom = 1;
        this.pan = 0;
        this.tilt = 0;
    }

    public synchronized PTZCameraState getState() {
        return PTZCameraState.newBuilder()
                .setPowerState(this.powerState)
                .setZoomLevel(this.zoom)
                .setPanDegrees(this.pan)
                .setTiltDegrees(this.tilt)
                .build();
    }

    public DeviceIdentity getIdentity() { return this.identity; }

    public synchronized void setPowerState(PowerState state) { 
        this.powerState = state; 
    }

    public synchronized void setZoom(int zoom) {
        this.zoom = zoom;
    }

    public synchronized void setPan(int pan) {
        this.pan = pan;
    }

    public synchronized void setTilt(int tilt) {
        this.tilt = tilt;
    }

    @Override
    public DeviceInfo getDeviceInfo(String serverLocation) {
        return DeviceInfo.newBuilder()
                .setIdentity(this.identity)
                .setType(DeviceType.PTZ_CAMERA)
                .setName(this.name)
                .setServerLocation(serverLocation)
                .build();
    }
}
