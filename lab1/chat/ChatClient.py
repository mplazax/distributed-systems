import socket
import threading

class ChatClient:
    def __init__(self, host='localhost', port=12212):
        self.host = host
        self.port = port
        self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_sock.bind(('', 0))  # Random port
        self.my_udp_addr = ('127.0.0.1', self.udp_sock.getsockname()[1])

    def connect_to_server(self) -> bool:
        try:
            self.tcp_sock.connect((self.host, self.port))
            self.tcp_sock.send(f"UDP_ADDR:{self.my_udp_addr[0]}:{self.my_udp_addr[1]}".encode('utf-8'))
            return True
        except Exception as e:
            print(f"Error connecting to server: {e}")
            return False

    def receive_messages_tcp(self) -> None:
        try:
            while True:
                tcp_msg = self.tcp_sock.recv(1024).decode('utf-8')
                if not tcp_msg:
                    break
                print(f"TCP: {tcp_msg}")
        except Exception as e:
            print(f"Error receiving TCP message: {e}")
        finally:
            self.tcp_sock.close()

    def receive_messages_udp(self) -> None:
        self.udp_sock.settimeout(1.0)
        try:
            while True:
                try:
                    udp_msg, server = self.udp_sock.recvfrom(1024)
                    print(f"UDP: {udp_msg.decode('utf-8')}")
                except socket.timeout:
                    continue
        except Exception as e:
            print(f"Error receiving UDP message: {e}")
        finally:
            self.udp_sock.close()

    def send_messages(self) -> None:
        try:
            while True:
                msg = input("")
                if msg.lower() == 'quit':
                    break
                if msg.startswith("U "):
                    udp_msg = msg[2:]
                    self.udp_sock.sendto(udp_msg.encode('utf-8'), (self.host, self.port))
                else:
                    self.tcp_sock.send(msg.encode('utf-8'))
        except Exception as e:
            print(f"Error sending message: {e}")
        finally:
            self.tcp_sock.close()

    def run(self) -> None:
        if not self.connect_to_server():
            return
        threading.Thread(target=self.receive_messages_tcp).start()
        threading.Thread(target=self.receive_messages_udp).start()
        self.send_messages()

if __name__ == '__main__':
    client = ChatClient()
    client.run()