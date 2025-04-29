package pl.agh.edu.sr.smarthome.server.services; // Zmień na swój pakiet

import com.google.protobuf.Empty;
import io.grpc.stub.StreamObserver;
import pl.agh.edu.sr.smarthome.generated.DeviceDiscoveryGrpc;
import pl.agh.edu.sr.smarthome.generated.ListDevicesResponse;
import pl.agh.edu.sr.smarthome.server.DeviceRepository; // Importuj repozytorium

public class DeviceDiscoveryImpl extends DeviceDiscoveryGrpc.DeviceDiscoveryImplBase {

    private final DeviceRepository repository;

    public DeviceDiscoveryImpl(DeviceRepository repository) {
        this.repository = repository;
    }

    @Override
    public void listDevices(Empty request, StreamObserver<ListDevicesResponse> responseObserver) {
        System.out.println("Received ListDevices request");
        // Pobierz listę DeviceInfo z repozytorium
        ListDevicesResponse response = ListDevicesResponse.newBuilder()
                .addAllDevices(repository.getAllDeviceInfo())
                .build();

        // Wyślij odpowiedź do klienta
        responseObserver.onNext(response);
        // Zakończ przetwarzanie RPC
        responseObserver.onCompleted();
        System.out.println("Sent " + response.getDevicesCount() + " devices");
    }
}