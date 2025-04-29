package pl.agh.edu.sr.smarthome.server.devices;

import pl.agh.edu.sr.smarthome.generated.DeviceInfo;
import pl.agh.edu.sr.smarthome.generated.DeviceIdentity;

public interface SmartDevice {
    DeviceInfo getDeviceInfo(String serverLocation);
    DeviceIdentity getIdentity();
}
