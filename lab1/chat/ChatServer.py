import socket
import threading

class ChatServer:
    def __init__(self, host='localhost', port=12212):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clients = []
        self.clients_lock = threading.Lock()

    def start(self) -> None:
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            print(f"ChatServer is running on {self.host}:{self.port}")
        except Exception as e:
            print(f"Error starting server: {e}")
            return

        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                thread.start()
        except KeyboardInterrupt:
            print("\nTerminating server...")
        finally:
            self.server_socket.close()

    def broadcast(self, message: str, sender_socket: socket.socket = None) -> None:
        with self.clients_lock:
            for sock, name in self.clients:
                if sock != sender_socket:
                    try:
                        sock.send(message.encode('utf-8'))
                    except Exception:
                        self.remove_client(sock)

    def remove_client(self, client_socket: socket.socket) -> None:
        with self.clients_lock:
            for i, (sock, name) in enumerate(self.clients):
                if sock == client_socket:
                    self.clients.pop(i)
                    print(f"Client {name} has been disconnected")
                    self.broadcast(f"{name} has left the chat room.")
                    break
        client_socket.close()

    def handle_client(self, client_socket: socket.socket, client_address: tuple) -> None:
        try:
            client_socket.send("Provide Username: ".encode('utf-8'))
            client_name = client_socket.recv(1024).decode('utf-8').strip()
        except Exception as e:
            print(f"Error client initialization: {e}")
            client_socket.close()
            return

        with self.clients_lock:
            self.clients.append((client_socket, client_name))
        print(f"Client {client_name} connected to {client_address}")
        self.broadcast(f"{client_name} has joined the chat room!")

        try:
            while True:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                self.broadcast(f"{client_name}: {data}", client_socket)
        except Exception:
            pass
        finally:
            self.remove_client(client_socket)

if __name__ == '__main__':
    server = ChatServer()
    server.start()
