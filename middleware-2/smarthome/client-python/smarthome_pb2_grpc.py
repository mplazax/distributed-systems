# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import smarthome_pb2 as smarthome__pb2

GRPC_GENERATED_VERSION = '1.69.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in smarthome_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class DeviceDiscoveryStub(object):
    """--- Services ---

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListDevices = channel.unary_unary(
                '/smarthome.DeviceDiscovery/ListDevices',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=smarthome__pb2.ListDevicesResponse.FromString,
                _registered_method=True)


class DeviceDiscoveryServicer(object):
    """--- Services ---

    """

    def ListDevices(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeviceDiscoveryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListDevices': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDevices,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=smarthome__pb2.ListDevicesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'smarthome.DeviceDiscovery', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('smarthome.DeviceDiscovery', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DeviceDiscovery(object):
    """--- Services ---

    """

    @staticmethod
    def ListDevices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/smarthome.DeviceDiscovery/ListDevices',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            smarthome__pb2.ListDevicesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class LightControlStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLightState = channel.unary_unary(
                '/smarthome.LightControl/GetLightState',
                request_serializer=smarthome__pb2.DeviceIdentity.SerializeToString,
                response_deserializer=smarthome__pb2.LightState.FromString,
                _registered_method=True)
        self.SetPower = channel.unary_unary(
                '/smarthome.LightControl/SetPower',
                request_serializer=smarthome__pb2.SetPowerRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.SetBrightness = channel.unary_unary(
                '/smarthome.LightControl/SetBrightness',
                request_serializer=smarthome__pb2.SetBrightnessRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class LightControlServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetLightState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPower(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetBrightness(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LightControlServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetLightState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLightState,
                    request_deserializer=smarthome__pb2.DeviceIdentity.FromString,
                    response_serializer=smarthome__pb2.LightState.SerializeToString,
            ),
            'SetPower': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPower,
                    request_deserializer=smarthome__pb2.SetPowerRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetBrightness': grpc.unary_unary_rpc_method_handler(
                    servicer.SetBrightness,
                    request_deserializer=smarthome__pb2.SetBrightnessRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'smarthome.LightControl', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('smarthome.LightControl', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class LightControl(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetLightState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/smarthome.LightControl/GetLightState',
            smarthome__pb2.DeviceIdentity.SerializeToString,
            smarthome__pb2.LightState.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetPower(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/smarthome.LightControl/SetPower',
            smarthome__pb2.SetPowerRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetBrightness(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/smarthome.LightControl/SetBrightness',
            smarthome__pb2.SetBrightnessRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class ThermostatControlStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetThermostatState = channel.unary_unary(
                '/smarthome.ThermostatControl/GetThermostatState',
                request_serializer=smarthome__pb2.DeviceIdentity.SerializeToString,
                response_deserializer=smarthome__pb2.ThermostatState.FromString,
                _registered_method=True)
        self.SetPower = channel.unary_unary(
                '/smarthome.ThermostatControl/SetPower',
                request_serializer=smarthome__pb2.SetPowerRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.SetTargetTemperature = channel.unary_unary(
                '/smarthome.ThermostatControl/SetTargetTemperature',
                request_serializer=smarthome__pb2.SetTemperatureRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.SetMode = channel.unary_unary(
                '/smarthome.ThermostatControl/SetMode',
                request_serializer=smarthome__pb2.SetModeRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class ThermostatControlServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetThermostatState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPower(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetTargetTemperature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetMode(self, request, context):
        """SetMode powinno być wywoływane tylko dla termostatów ADVANCED
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ThermostatControlServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetThermostatState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetThermostatState,
                    request_deserializer=smarthome__pb2.DeviceIdentity.FromString,
                    response_serializer=smarthome__pb2.ThermostatState.SerializeToString,
            ),
            'SetPower': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPower,
                    request_deserializer=smarthome__pb2.SetPowerRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetTargetTemperature': grpc.unary_unary_rpc_method_handler(
                    servicer.SetTargetTemperature,
                    request_deserializer=smarthome__pb2.SetTemperatureRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetMode': grpc.unary_unary_rpc_method_handler(
                    servicer.SetMode,
                    request_deserializer=smarthome__pb2.SetModeRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'smarthome.ThermostatControl', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('smarthome.ThermostatControl', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ThermostatControl(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetThermostatState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/smarthome.ThermostatControl/GetThermostatState',
            smarthome__pb2.DeviceIdentity.SerializeToString,
            smarthome__pb2.ThermostatState.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetPower(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/smarthome.ThermostatControl/SetPower',
            smarthome__pb2.SetPowerRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetTargetTemperature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/smarthome.ThermostatControl/SetTargetTemperature',
            smarthome__pb2.SetTemperatureRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/smarthome.ThermostatControl/SetMode',
            smarthome__pb2.SetModeRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class CameraControlStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPTZCameraState = channel.unary_unary(
                '/smarthome.CameraControl/GetPTZCameraState',
                request_serializer=smarthome__pb2.DeviceIdentity.SerializeToString,
                response_deserializer=smarthome__pb2.PTZCameraState.FromString,
                _registered_method=True)
        self.SetPower = channel.unary_unary(
                '/smarthome.CameraControl/SetPower',
                request_serializer=smarthome__pb2.SetPowerRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.SetPTZ = channel.unary_unary(
                '/smarthome.CameraControl/SetPTZ',
                request_serializer=smarthome__pb2.SetPTZRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class CameraControlServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPTZCameraState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPower(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPTZ(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CameraControlServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPTZCameraState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPTZCameraState,
                    request_deserializer=smarthome__pb2.DeviceIdentity.FromString,
                    response_serializer=smarthome__pb2.PTZCameraState.SerializeToString,
            ),
            'SetPower': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPower,
                    request_deserializer=smarthome__pb2.SetPowerRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetPTZ': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPTZ,
                    request_deserializer=smarthome__pb2.SetPTZRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'smarthome.CameraControl', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('smarthome.CameraControl', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CameraControl(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPTZCameraState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/smarthome.CameraControl/GetPTZCameraState',
            smarthome__pb2.DeviceIdentity.SerializeToString,
            smarthome__pb2.PTZCameraState.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetPower(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/smarthome.CameraControl/SetPower',
            smarthome__pb2.SetPowerRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetPTZ(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/smarthome.CameraControl/SetPTZ',
            smarthome__pb2.SetPTZRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
