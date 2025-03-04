import socket
import threading

class ChatServer:
    def __init__(self, host='127.0.0.1', port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clients = []  # Lista przechowująca krotki: (socket, nazwa użytkownika)
        self.clients_lock = threading.Lock()

    def start(self) -> None:
        """Uruchamia serwer, wiąże gniazdo i nasłuchuje połączeń."""
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            print(f"Serwer działa na {self.host}:{self.port}")
        except Exception as e:
            print(f"Błąd serwera: {e}")
            return

        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                thread.start()
        except KeyboardInterrupt:
            print("\nPrzerywanie działania serwera...")
        finally:
            self.server_socket.close()

    def broadcast(self, message: str, sender_socket: socket.socket = None) -> None:
        """Rozsyła wiadomość do wszystkich połączonych klientów poza nadawcą."""
        with self.clients_lock:
            for sock, name in self.clients:
                if sock != sender_socket:
                    try:
                        sock.send(message.encode('utf-8'))
                    except Exception:
                        self.remove_client(sock)

    def remove_client(self, client_socket: socket.socket) -> None:
        """Usuwa klienta z listy i zamyka jego połączenie."""
        with self.clients_lock:
            for i, (sock, name) in enumerate(self.clients):
                if sock == client_socket:
                    self.clients.pop(i)
                    print(f"Klient {name} został rozłączony.")
                    self.broadcast(f"{name} opuścił czat.")
                    break
        client_socket.close()

    def handle_client(self, client_socket: socket.socket, client_address: tuple) -> None:
        """Obsługuje komunikację z pojedynczym klientem."""
        try:
            client_socket.send("Podaj nazwę użytkownika: ".encode('utf-8'))
            client_name = client_socket.recv(1024).decode('utf-8').strip()
        except Exception as e:
            print(f"Błąd przy inicjalizacji klienta: {e}")
            client_socket.close()
            return

        with self.clients_lock:
            self.clients.append((client_socket, client_name))
        print(f"Klient {client_name} połączony z {client_address}")
        self.broadcast(f"{client_name} dołączył do czatu!")

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
