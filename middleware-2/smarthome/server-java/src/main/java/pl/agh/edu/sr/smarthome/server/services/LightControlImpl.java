package pl.agh.edu.sr.smarthome.server.services;

import com.google.protobuf.Empty;
import io.grpc.Status;
import io.grpc.stub.StreamObserver;
import pl.agh.edu.sr.smarthome.generated.*;
import pl.agh.edu.sr.smarthome.server.DeviceRepository;

public class LightControlImpl extends LightControlGrpc.LightControlImplBase {

    private final DeviceRepository repository;

    public LightControlImpl(DeviceRepository repository) {
        this.repository = repository;
    }

    @Override
    public void getLightState(DeviceIdentity request, StreamObserver<LightState> responseObserver) {
        System.out.println("Received GetLightState request for ID: " + request.getId());
        repository.findLight(request.getId())
                .ifPresentOrElse(
                        light -> {
                            responseObserver.onNext(light.getState());
                            responseObserver.onCompleted();
                            System.out.println("Sent light state for ID: " + request.getId());
                        },
                        () -> {
                            System.err.println("Light not found for ID: " + request.getId());
                            responseObserver.onError(Status.NOT_FOUND
                                    .withDescription("Light not found: " + request.getId())
                                    .asRuntimeException());
                        }
                );
    }

    @Override
    public void setPower(SetPowerRequest request, StreamObserver<Empty> responseObserver) {
        String id = request.getIdentity().getId();
        PowerState desiredState = request.getDesiredPowerState();
        System.out.println("Received SetPower request for ID: " + id + " to " + desiredState);

        repository.findLight(id)
                .ifPresentOrElse(
                        light -> {
                            try {
                                light.setPowerState(desiredState);
                                responseObserver.onNext(Empty.newBuilder().build());
                                responseObserver.onCompleted();
                                System.out.println("Successfully set power for ID: " + id);
                            } catch (Exception e) { 
                                System.err.println("Error setting power for ID: " + id + " - " + e.getMessage());
                                responseObserver.onError(Status.INTERNAL
                                        .withDescription("Error setting power: " + e.getMessage())
                                        .withCause(e)
                                        .asRuntimeException());
                            }
                        },
                        () -> {
                            System.err.println("Light not found for ID: " + id);
                            responseObserver.onError(Status.NOT_FOUND
                                    .withDescription("Light not found: " + id)
                                    .asRuntimeException());
                        }
                );
    }

    @Override
    public void setBrightness(SetBrightnessRequest request, StreamObserver<Empty> responseObserver) {
        String id = request.getIdentity().getId();
        int brightness = request.getDesiredBrightnessPercentage();
        System.out.println("Received SetBrightness request for ID: " + id + " to " + brightness + "%");

        if (brightness < 0 || brightness > 100) {
            System.err.println("Invalid brightness value for ID: " + id + " - " + brightness);
            responseObserver.onError(Status.INVALID_ARGUMENT
                    .withDescription("Brightness must be between 0 and 100")
                    .asRuntimeException());
            return;
        }

        repository.findLight(id)
                .ifPresentOrElse(
                        light -> {
                            try {
                                light.setBrightness(brightness);
                                responseObserver.onNext(Empty.newBuilder().build());
                                responseObserver.onCompleted();
                                 System.out.println("Successfully set brightness for ID: " + id);
                            } catch (IllegalArgumentException e) { 
                                 System.err.println("Error setting brightness for ID: " + id + " - " + e.getMessage());
                                 responseObserver.onError(Status.INVALID_ARGUMENT
                                        .withDescription(e.getMessage())
                                        .asRuntimeException());
                            }
                            catch (Exception e) { 
                                 System.err.println("Internal error setting brightness for ID: " + id + " - " + e.getMessage());
                                responseObserver.onError(Status.INTERNAL
                                        .withDescription("Error setting brightness: " + e.getMessage())
                                        .withCause(e)
                                        .asRuntimeException());
                            }
                        },
                        () -> {
                             System.err.println("Light not found for ID: " + id);
                            responseObserver.onError(Status.NOT_FOUND
                                    .withDescription("Light not found: " + id)
                                    .asRuntimeException());
                        }
                );
    }
}