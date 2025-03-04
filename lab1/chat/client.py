import socket
import threading

class ChatClient:
    def __init__(self, host='127.0.0.1', port=12345):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self) -> bool:
        """Nawiązuje połączenie z serwerem."""
        try:
            self.sock.connect((self.host, self.port))
            return True
        except Exception as e:
            print(f"Błąd połączenia: {e}")
            return False

    def receive_messages(self) -> None:
        """Odbiera wiadomości z serwera i wyświetla je."""
        try:
            while True:
                data = self.sock.recv(1024).decode('utf-8')
                if not data:
                    break
                print(data)
        except Exception as e:
            print(f"Błąd odbierania wiadomości: {e}")
        finally:
            self.sock.close()

    def send_messages(self) -> None:
        """Wysyła wiadomości wpisane przez użytkownika do serwera"""
        try:
            while True:
                message = input("")
                if message.lower() == 'quit':
                    break
                self.sock.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Błąd wysyłania wiadomości: {e}")
        finally:
            self.sock.close()

    def run(self) -> None:
        """Uruchamia klienta – łączy się z serwerem i startuje wątki wysyłania oraz odbierania wiadomości."""
        if not self.connect_to_server():
            return

        thread_receive = threading.Thread(target=self.receive_messages)
        thread_send = threading.Thread(target=self.send_messages)
        thread_receive.start()
        thread_send.start()

        thread_send.join()
        thread_receive.join()

if __name__ == '__main__':
    client = ChatClient()
    client.run()
