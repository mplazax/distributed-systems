# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: smarthome.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'smarthome.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fsmarthome.proto\x12\tsmarthome\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x1c\n\x0e\x44\x65viceIdentity\x12\n\n\x02id\x18\x01 \x01(\t\"\xdb\x01\n\nDeviceInfo\x12+\n\x08identity\x18\x01 \x01(\x0b\x32\x19.smarthome.DeviceIdentity\x12#\n\x04type\x18\x02 \x01(\x0e\x32\x15.smarthome.DeviceType\x12\x0c\n\x04name\x18\x03 \x01(\t\x12=\n\x12thermostat_subtype\x18\x04 \x01(\x0e\x32\x1c.smarthome.ThermostatSubtypeH\x00\x88\x01\x01\x12\x17\n\x0fserver_location\x18\x05 \x01(\tB\x15\n\x13_thermostat_subtype\"W\n\nLightState\x12*\n\x0bpower_state\x18\x01 \x01(\x0e\x32\x15.smarthome.PowerState\x12\x1d\n\x15\x62rightness_percentage\x18\x02 \x01(\x05\"\xbd\x01\n\x0fThermostatState\x12*\n\x0bpower_state\x18\x01 \x01(\x0e\x32\x15.smarthome.PowerState\x12\"\n\x1atarget_temperature_celsius\x18\x02 \x01(\x02\x12#\n\x1b\x63urrent_temperature_celsius\x18\x03 \x01(\x02\x12,\n\x04mode\x18\x04 \x01(\x0e\x32\x19.smarthome.ThermostatModeH\x00\x88\x01\x01\x42\x07\n\x05_mode\"{\n\x0ePTZCameraState\x12*\n\x0bpower_state\x18\x01 \x01(\x0e\x32\x15.smarthome.PowerState\x12\x13\n\x0bpan_degrees\x18\x02 \x01(\x05\x12\x14\n\x0ctilt_degrees\x18\x03 \x01(\x05\x12\x12\n\nzoom_level\x18\x04 \x01(\x05\"r\n\x0fSetPowerRequest\x12+\n\x08identity\x18\x01 \x01(\x0b\x32\x19.smarthome.DeviceIdentity\x12\x32\n\x13\x64\x65sired_power_state\x18\x02 \x01(\x0e\x32\x15.smarthome.PowerState\"j\n\x14SetBrightnessRequest\x12+\n\x08identity\x18\x01 \x01(\x0b\x32\x19.smarthome.DeviceIdentity\x12%\n\x1d\x64\x65sired_brightness_percentage\x18\x02 \x01(\x05\"p\n\x15SetTemperatureRequest\x12+\n\x08identity\x18\x01 \x01(\x0b\x32\x19.smarthome.DeviceIdentity\x12*\n\"desired_target_temperature_celsius\x18\x02 \x01(\x02\"n\n\x0eSetModeRequest\x12+\n\x08identity\x18\x01 \x01(\x0b\x32\x19.smarthome.DeviceIdentity\x12/\n\x0c\x64\x65sired_mode\x18\x02 \x01(\x0e\x32\x19.smarthome.ThermostatMode\"\xea\x01\n\rSetPTZRequest\x12+\n\x08identity\x18\x01 \x01(\x0b\x32\x19.smarthome.DeviceIdentity\x12\x38\n\x13\x64\x65sired_pan_degrees\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x39\n\x14\x64\x65sired_tilt_degrees\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x37\n\x12\x64\x65sired_zoom_level\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\"=\n\x13ListDevicesResponse\x12&\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x15.smarthome.DeviceInfo*`\n\nDeviceType\x12\x17\n\x13UNKNOWN_DEVICE_TYPE\x10\x00\x12\t\n\x05LIGHT\x10\x01\x12\x0e\n\nTHERMOSTAT\x10\x02\x12\x0e\n\nPTZ_CAMERA\x10\x03\x12\x0e\n\nBULBULATOR\x10\x04*B\n\x11ThermostatSubtype\x12\x13\n\x0fUNKNOWN_SUBTYPE\x10\x00\x12\n\n\x06SIMPLE\x10\x01\x12\x0c\n\x08\x41\x44VANCED\x10\x02*\x1d\n\nPowerState\x12\x07\n\x03OFF\x10\x00\x12\x06\n\x02ON\x10\x01*<\n\x0eThermostatMode\x12\x08\n\x04HEAT\x10\x00\x12\x08\n\x04\x43OOL\x10\x01\x12\x0c\n\x08\x46\x41N_ONLY\x10\x02\x12\x08\n\x04\x41UTO\x10\x03\x32X\n\x0f\x44\x65viceDiscovery\x12\x45\n\x0bListDevices\x12\x16.google.protobuf.Empty\x1a\x1e.smarthome.ListDevicesResponse2\xdb\x01\n\x0cLightControl\x12\x41\n\rGetLightState\x12\x19.smarthome.DeviceIdentity\x1a\x15.smarthome.LightState\x12>\n\x08SetPower\x12\x1a.smarthome.SetPowerRequest\x1a\x16.google.protobuf.Empty\x12H\n\rSetBrightness\x12\x1f.smarthome.SetBrightnessRequest\x1a\x16.google.protobuf.Empty2\xb0\x02\n\x11ThermostatControl\x12K\n\x12GetThermostatState\x12\x19.smarthome.DeviceIdentity\x1a\x1a.smarthome.ThermostatState\x12>\n\x08SetPower\x12\x1a.smarthome.SetPowerRequest\x1a\x16.google.protobuf.Empty\x12P\n\x14SetTargetTemperature\x12 .smarthome.SetTemperatureRequest\x1a\x16.google.protobuf.Empty\x12<\n\x07SetMode\x12\x19.smarthome.SetModeRequest\x1a\x16.google.protobuf.Empty2\xd6\x01\n\rCameraControl\x12I\n\x11GetPTZCameraState\x12\x19.smarthome.DeviceIdentity\x1a\x19.smarthome.PTZCameraState\x12>\n\x08SetPower\x12\x1a.smarthome.SetPowerRequest\x1a\x16.google.protobuf.Empty\x12:\n\x06SetPTZ\x12\x18.smarthome.SetPTZRequest\x1a\x16.google.protobuf.EmptyB5\n!pl.agh.edu.sr.smarthome.generatedB\x0eSmartHomeProtoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'smarthome_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!pl.agh.edu.sr.smarthome.generatedB\016SmartHomeProtoP\001'
  _globals['_DEVICETYPE']._serialized_start=1499
  _globals['_DEVICETYPE']._serialized_end=1595
  _globals['_THERMOSTATSUBTYPE']._serialized_start=1597
  _globals['_THERMOSTATSUBTYPE']._serialized_end=1663
  _globals['_POWERSTATE']._serialized_start=1665
  _globals['_POWERSTATE']._serialized_end=1694
  _globals['_THERMOSTATMODE']._serialized_start=1696
  _globals['_THERMOSTATMODE']._serialized_end=1756
  _globals['_DEVICEIDENTITY']._serialized_start=91
  _globals['_DEVICEIDENTITY']._serialized_end=119
  _globals['_DEVICEINFO']._serialized_start=122
  _globals['_DEVICEINFO']._serialized_end=341
  _globals['_LIGHTSTATE']._serialized_start=343
  _globals['_LIGHTSTATE']._serialized_end=430
  _globals['_THERMOSTATSTATE']._serialized_start=433
  _globals['_THERMOSTATSTATE']._serialized_end=622
  _globals['_PTZCAMERASTATE']._serialized_start=624
  _globals['_PTZCAMERASTATE']._serialized_end=747
  _globals['_SETPOWERREQUEST']._serialized_start=749
  _globals['_SETPOWERREQUEST']._serialized_end=863
  _globals['_SETBRIGHTNESSREQUEST']._serialized_start=865
  _globals['_SETBRIGHTNESSREQUEST']._serialized_end=971
  _globals['_SETTEMPERATUREREQUEST']._serialized_start=973
  _globals['_SETTEMPERATUREREQUEST']._serialized_end=1085
  _globals['_SETMODEREQUEST']._serialized_start=1087
  _globals['_SETMODEREQUEST']._serialized_end=1197
  _globals['_SETPTZREQUEST']._serialized_start=1200
  _globals['_SETPTZREQUEST']._serialized_end=1434
  _globals['_LISTDEVICESRESPONSE']._serialized_start=1436
  _globals['_LISTDEVICESRESPONSE']._serialized_end=1497
  _globals['_DEVICEDISCOVERY']._serialized_start=1758
  _globals['_DEVICEDISCOVERY']._serialized_end=1846
  _globals['_LIGHTCONTROL']._serialized_start=1849
  _globals['_LIGHTCONTROL']._serialized_end=2068
  _globals['_THERMOSTATCONTROL']._serialized_start=2071
  _globals['_THERMOSTATCONTROL']._serialized_end=2375
  _globals['_CAMERACONTROL']._serialized_start=2378
  _globals['_CAMERACONTROL']._serialized_end=2592
# @@protoc_insertion_point(module_scope)
