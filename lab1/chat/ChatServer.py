import socket
import threading

class ChatServer:
    def __init__(self, host='localhost', port=12212):
        self.host = host
        self.port = port
        self.server_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.clients = []  # (socket TCP, name, address TCP, address UDP)
        self.clients_lock = threading.Lock()

    def start(self) -> None:
        try:
            self.server_socket_tcp.bind((self.host, self.port))
            self.server_socket_tcp.listen(5)
            print(f"ChatServer TCP is running on {self.host}:{self.port}")
            self.server_socket_udp.bind((self.host, self.port))
            print(f"ChatServer UDP is listening on {self.host}:{self.port}")
            threading.Thread(target=self.handle_udp).start()
        except Exception as e:
            print(f"Error starting server: {e}")
            return

        try:
            while True:
                client_socket, client_address = self.server_socket_tcp.accept()
                threading.Thread(target=self.handle_client, args=(client_socket, client_address)).start()
        except KeyboardInterrupt:
            print("\nTerminating server...")
        finally:
            self.server_socket_tcp.close()

    def broadcast(self, message: str, sender_socket=None, sender_addr=None) -> None:
        with self.clients_lock:
            if sender_addr:  # UDP broadcast
                for sock, name, tcp_addr, udp_addr in self.clients:
                    if udp_addr != sender_addr:
                        try:
                            self.server_socket_udp.sendto(message.encode('utf-8'), udp_addr)
                            print(f"UDP MESSAGE SENT TO: {name} at {udp_addr}")
                        except Exception as e:
                            print(f"Failed to send UDP to {name} at {udp_addr}: {e}")
            else:  # TCP broadcast
                for sock, name, tcp_addr, udp_addr in self.clients:
                    if sock != sender_socket:
                        try:
                            sock.send(message.encode('utf-8'))
                        except:
                            self.remove_client(sock)

    def remove_client(self, client_socket: socket.socket) -> None:
        with self.clients_lock:
            for i, (sock, name, tcp_addr, udp_addr) in enumerate(self.clients):
                if sock == client_socket:
                    self.clients.pop(i)
                    print(f"Client {name} has been disconnected")
                    self.broadcast(f"{name} has left the chat room.")
                    break
        client_socket.close()

    def handle_client(self, client_socket: socket.socket, client_address: tuple) -> None:
        try:
            udp_info = client_socket.recv(1024).decode('utf-8')
            if udp_info.startswith("UDP_ADDR:"):
                udp_host, udp_port = udp_info.split(":")[1], int(udp_info.split(":")[2])
                udp_addr = (udp_host, udp_port)
                print(f"Client registered UDP address: {udp_addr}")
            else:
                udp_addr = None
            client_socket.send("Provide Username: ".encode('utf-8'))
            client_name = client_socket.recv(1024).decode('utf-8').strip()
        except Exception as e:
            print(f"Error client initialization: {e}")
            client_socket.close()
            return

        with self.clients_lock:
            self.clients.append((client_socket, client_name, client_address, udp_addr))
        print(f"Client {client_name} connected to {client_address} with UDP {udp_addr}")
        self.broadcast(f"{client_name} has joined the chat room!", sender_socket=client_socket)

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

    def handle_udp(self) -> None:
        while True:
            try:
                data, address = self.server_socket_udp.recvfrom(1024)
                message = data.decode('utf-8').strip()
                print(f"UDP from {address}: {message}")
                sender_name = "Unknown"
                with self.clients_lock:
                    for _, name, _, udp_addr in self.clients:
                        if udp_addr == address:
                            sender_name = name
                            break
                self.broadcast(f"{sender_name}: {message}", sender_addr=address)
            except Exception as e:
                print(f"UDP error: {e}")

if __name__ == '__main__':
    server = ChatServer()
    server.start()