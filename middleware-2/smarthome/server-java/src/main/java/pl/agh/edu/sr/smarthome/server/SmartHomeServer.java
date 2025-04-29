package pl.agh.edu.sr.smarthome.server;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import pl.agh.edu.sr.smarthome.server.services.*;

import java.io.IOException;
import java.util.concurrent.TimeUnit;

public class SmartHomeServer {

    private Server server;
    private final int port;
    private final DeviceRepository repository;

    public SmartHomeServer(int port) {
        this.port = port;
        String serverLocation = "localhost:" + port;
        this.repository = new DeviceRepository(serverLocation);
    }

    public void start() throws IOException {
        repository.initializeWithSampleDevices();
        server = ServerBuilder.forPort(port)
                .addService(new DeviceDiscoveryImpl(repository))
                .addService(new LightControlImpl(repository))
                .addService(new ThermostatControlImpl(repository))
                .addService(new CameraControlImpl(repository))
                .build()
                .start();

        System.out.println("--------------------------------------------------");
        System.out.println(" SmartHome Server started on port: " + port);
        System.out.println("--------------------------------------------------");

        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            System.err.println("*** shutting down gRPC server since JVM is shutting down");
            try {
                SmartHomeServer.this.stop();
            } catch (InterruptedException e) {
                e.printStackTrace(System.err);
                Thread.currentThread().interrupt();
            }
            System.err.println("*** server shut down");
        }));
    }

    public void stop() throws InterruptedException {
        if (server != null) {
            server.shutdown().awaitTermination(30, TimeUnit.SECONDS);
        }
    }

    private void blockUntilShutdown() throws InterruptedException {
        if (server != null) {
            server.awaitTermination();
        }
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        int port = 50051;
        if (args.length > 0) {
            try {
                port = Integer.parseInt(args[0]);
            } catch (NumberFormatException e) {
                System.err.println("Invalid port number provided: " + args[0] + ". Using default " + port);
            }
        }

        final SmartHomeServer server = new SmartHomeServer(port);
        server.start();
        server.blockUntilShutdown();
    }
}