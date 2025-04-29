package pl.agh.edu.sr.smarthome.server.services;

import com.google.protobuf.Empty;
import io.grpc.Status;
import io.grpc.stub.StreamObserver;
import pl.agh.edu.sr.smarthome.generated.*;
import pl.agh.edu.sr.smarthome.server.DeviceRepository;

public class CameraControlImpl extends CameraControlGrpc.CameraControlImplBase {

    private final DeviceRepository repository;

    public CameraControlImpl(DeviceRepository repository) {
        this.repository = repository;
    }

    @Override
    public void getPTZCameraState(DeviceIdentity request, StreamObserver<PTZCameraState> responseObserver) {
        System.out.println("Received GetPTZCameraState request for ID: " + request.getId());
        repository.findCamera(request.getId())
                .ifPresentOrElse(
                        camera -> {
                            responseObserver.onNext(camera.getState());
                            responseObserver.onCompleted();
                            System.out.println("Sent camera state for ID: " + request.getId());
                        },
                        () -> {
                            System.err.println("Camera not found for ID: " + request.getId());
                            responseObserver.onError(Status.NOT_FOUND
                                    .withDescription("Camera not found: " + request.getId())
                                    .asRuntimeException());
                        }
                );
    }

    @Override
    public void setPower(SetPowerRequest request, StreamObserver<Empty> responseObserver) {
        System.out.println("Received SetPower request for camera ID: " + request.getIdentity().getId());
        repository.findCamera(request.getIdentity().getId())
                .ifPresentOrElse(
                        camera -> {
                            camera.setPowerState(request.getDesiredPowerState());
                            responseObserver.onNext(Empty.getDefaultInstance());
                            responseObserver.onCompleted();
                            System.out.println("Set power state for camera ID: " + request.getIdentity().getId());
                        },
                        () -> {
                            System.err.println("Camera not found for ID: " + request.getIdentity().getId());
                            responseObserver.onError(Status.NOT_FOUND
                                    .withDescription("Camera not found: " + request.getIdentity().getId())
                                    .asRuntimeException());
                        }
                );
    }

    @Override
    public void setPTZ(SetPTZRequest request, StreamObserver<Empty> responseObserver) {
        System.out.println("Received SetPTZ request for camera ID: " + request.getIdentity().getId());
        repository.findCamera(request.getIdentity().getId())
                .ifPresentOrElse(
                        camera -> {
                            if (request.hasDesiredPanDegrees()) {
                                camera.setPan(request.getDesiredPanDegrees().getValue());
                            }
                            if (request.hasDesiredTiltDegrees()) {
                                camera.setTilt(request.getDesiredTiltDegrees().getValue());
                            }
                            if (request.hasDesiredZoomLevel()) {
                                camera.setZoom(request.getDesiredZoomLevel().getValue());
                            }
                            responseObserver.onNext(Empty.getDefaultInstance());
                            responseObserver.onCompleted();
                            System.out.println("Set PTZ for camera ID: " + request.getIdentity().getId());
                        },
                        () -> {
                            System.err.println("Camera not found for ID: " + request.getIdentity().getId());
                            responseObserver.onError(Status.NOT_FOUND
                                    .withDescription("Camera not found: " + request.getIdentity().getId())
                                    .asRuntimeException());
                        }
                );
    }
}