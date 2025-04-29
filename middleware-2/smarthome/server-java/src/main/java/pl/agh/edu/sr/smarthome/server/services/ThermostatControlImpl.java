package pl.agh.edu.sr.smarthome.server.services;

import com.google.protobuf.Empty;
import io.grpc.Status;
import io.grpc.stub.StreamObserver;
import pl.agh.edu.sr.smarthome.generated.*;
import pl.agh.edu.sr.smarthome.server.DeviceRepository;

public class ThermostatControlImpl extends ThermostatControlGrpc.ThermostatControlImplBase {
    private final DeviceRepository repository;

    public ThermostatControlImpl(DeviceRepository repository) {
        this.repository = repository;
    }

    @Override
    public void getThermostatState(DeviceIdentity request, StreamObserver<ThermostatState> responseObserver) {
        System.out.println("Received GetThermostatState request for ID: " + request.getId());
        repository.findThermostat(request.getId())
                .ifPresentOrElse(
                        thermostat -> {
                            responseObserver.onNext(thermostat.getState());
                            responseObserver.onCompleted();
                            System.out.println("Sent thermostat state for ID: " + request.getId());
                        },
                        () -> {
                            System.err.println("Thermostat not found for ID: " + request.getId());
                            responseObserver.onError(Status.NOT_FOUND
                                    .withDescription("Thermostat not found: " + request.getId())
                                    .asRuntimeException());
                        }
                );
    }

    @Override
    public void setPower(SetPowerRequest request, StreamObserver<Empty> responseObserver) {
        String id = request.getIdentity().getId();
        PowerState state = request.getDesiredPowerState();
        System.out.println("Received SetPower request for ID: " + id + " to " + state);

        repository.findThermostat(id)
                .ifPresentOrElse(
                        thermostat -> {
                            try {
                                thermostat.setPowerState(state);
                                responseObserver.onNext(Empty.newBuilder().build());
                                responseObserver.onCompleted();
                                System.out.println("Successfully set power state for ID: " + id);
                            } catch (Exception e) {
                                System.err.println("Internal error setting power state for ID: " + id + " - " + e.getMessage());
                                responseObserver.onError(Status.INTERNAL
                                        .withDescription("Error setting power state: " + e.getMessage())
                                        .withCause(e)
                                        .asRuntimeException());
                            }
                        },
                        () -> {
                            System.err.println("Thermostat not found for ID: " + id);
                            responseObserver.onError(Status.NOT_FOUND
                                    .withDescription("Thermostat not found: " + id)
                                    .asRuntimeException());
                        }
                );
    }
}