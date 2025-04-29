from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_DEVICE_TYPE: _ClassVar[DeviceType]
    LIGHT: _ClassVar[DeviceType]
    THERMOSTAT: _ClassVar[DeviceType]
    PTZ_CAMERA: _ClassVar[DeviceType]
    BULBULATOR: _ClassVar[DeviceType]

class ThermostatSubtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_SUBTYPE: _ClassVar[ThermostatSubtype]
    SIMPLE: _ClassVar[ThermostatSubtype]
    ADVANCED: _ClassVar[ThermostatSubtype]

class PowerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OFF: _ClassVar[PowerState]
    ON: _ClassVar[PowerState]

class ThermostatMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HEAT: _ClassVar[ThermostatMode]
    COOL: _ClassVar[ThermostatMode]
    FAN_ONLY: _ClassVar[ThermostatMode]
    AUTO: _ClassVar[ThermostatMode]
UNKNOWN_DEVICE_TYPE: DeviceType
LIGHT: DeviceType
THERMOSTAT: DeviceType
PTZ_CAMERA: DeviceType
BULBULATOR: DeviceType
UNKNOWN_SUBTYPE: ThermostatSubtype
SIMPLE: ThermostatSubtype
ADVANCED: ThermostatSubtype
OFF: PowerState
ON: PowerState
HEAT: ThermostatMode
COOL: ThermostatMode
FAN_ONLY: ThermostatMode
AUTO: ThermostatMode

class DeviceIdentity(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeviceInfo(_message.Message):
    __slots__ = ("identity", "type", "name", "thermostat_subtype", "server_location")
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    THERMOSTAT_SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    SERVER_LOCATION_FIELD_NUMBER: _ClassVar[int]
    identity: DeviceIdentity
    type: DeviceType
    name: str
    thermostat_subtype: ThermostatSubtype
    server_location: str
    def __init__(self, identity: _Optional[_Union[DeviceIdentity, _Mapping]] = ..., type: _Optional[_Union[DeviceType, str]] = ..., name: _Optional[str] = ..., thermostat_subtype: _Optional[_Union[ThermostatSubtype, str]] = ..., server_location: _Optional[str] = ...) -> None: ...

class LightState(_message.Message):
    __slots__ = ("power_state", "brightness_percentage")
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    BRIGHTNESS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    power_state: PowerState
    brightness_percentage: int
    def __init__(self, power_state: _Optional[_Union[PowerState, str]] = ..., brightness_percentage: _Optional[int] = ...) -> None: ...

class ThermostatState(_message.Message):
    __slots__ = ("power_state", "target_temperature_celsius", "current_temperature_celsius", "mode")
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    TARGET_TEMPERATURE_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TEMPERATURE_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    power_state: PowerState
    target_temperature_celsius: float
    current_temperature_celsius: float
    mode: ThermostatMode
    def __init__(self, power_state: _Optional[_Union[PowerState, str]] = ..., target_temperature_celsius: _Optional[float] = ..., current_temperature_celsius: _Optional[float] = ..., mode: _Optional[_Union[ThermostatMode, str]] = ...) -> None: ...

class PTZCameraState(_message.Message):
    __slots__ = ("power_state", "pan_degrees", "tilt_degrees", "zoom_level")
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    PAN_DEGREES_FIELD_NUMBER: _ClassVar[int]
    TILT_DEGREES_FIELD_NUMBER: _ClassVar[int]
    ZOOM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    power_state: PowerState
    pan_degrees: int
    tilt_degrees: int
    zoom_level: int
    def __init__(self, power_state: _Optional[_Union[PowerState, str]] = ..., pan_degrees: _Optional[int] = ..., tilt_degrees: _Optional[int] = ..., zoom_level: _Optional[int] = ...) -> None: ...

class SetPowerRequest(_message.Message):
    __slots__ = ("identity", "desired_power_state")
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    identity: DeviceIdentity
    desired_power_state: PowerState
    def __init__(self, identity: _Optional[_Union[DeviceIdentity, _Mapping]] = ..., desired_power_state: _Optional[_Union[PowerState, str]] = ...) -> None: ...

class SetBrightnessRequest(_message.Message):
    __slots__ = ("identity", "desired_brightness_percentage")
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_BRIGHTNESS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    identity: DeviceIdentity
    desired_brightness_percentage: int
    def __init__(self, identity: _Optional[_Union[DeviceIdentity, _Mapping]] = ..., desired_brightness_percentage: _Optional[int] = ...) -> None: ...

class SetTemperatureRequest(_message.Message):
    __slots__ = ("identity", "desired_target_temperature_celsius")
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_TARGET_TEMPERATURE_CELSIUS_FIELD_NUMBER: _ClassVar[int]
    identity: DeviceIdentity
    desired_target_temperature_celsius: float
    def __init__(self, identity: _Optional[_Union[DeviceIdentity, _Mapping]] = ..., desired_target_temperature_celsius: _Optional[float] = ...) -> None: ...

class SetModeRequest(_message.Message):
    __slots__ = ("identity", "desired_mode")
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_MODE_FIELD_NUMBER: _ClassVar[int]
    identity: DeviceIdentity
    desired_mode: ThermostatMode
    def __init__(self, identity: _Optional[_Union[DeviceIdentity, _Mapping]] = ..., desired_mode: _Optional[_Union[ThermostatMode, str]] = ...) -> None: ...

class SetPTZRequest(_message.Message):
    __slots__ = ("identity", "desired_pan_degrees", "desired_tilt_degrees", "desired_zoom_level")
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_PAN_DEGREES_FIELD_NUMBER: _ClassVar[int]
    DESIRED_TILT_DEGREES_FIELD_NUMBER: _ClassVar[int]
    DESIRED_ZOOM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    identity: DeviceIdentity
    desired_pan_degrees: _wrappers_pb2.Int32Value
    desired_tilt_degrees: _wrappers_pb2.Int32Value
    desired_zoom_level: _wrappers_pb2.Int32Value
    def __init__(self, identity: _Optional[_Union[DeviceIdentity, _Mapping]] = ..., desired_pan_degrees: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., desired_tilt_degrees: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., desired_zoom_level: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class ListDevicesResponse(_message.Message):
    __slots__ = ("devices",)
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[DeviceInfo]
    def __init__(self, devices: _Optional[_Iterable[_Union[DeviceInfo, _Mapping]]] = ...) -> None: ...
