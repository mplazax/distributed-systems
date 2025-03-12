import socket
import threading



class ChatClient:

    def __init__(self, host='localhost', port=12212):
        self.host = host
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    def connect_to_server(self) -> bool:
        try:
            self.sock.connect((self.host, self.port))
            return True

        except Exception as e:
            print(f"Error connecting to server: {e}")
            return False



    def receive_messages(self) -> None:

        try:
            while True:
                msg = self.sock.recv(1024).decode('utf-8')

                if not msg:
                    break

                print(msg)

        except Exception as e:
            print(f"Error receiving message: {e}")

        finally:
            self.sock.close()



    def send_messages(self) -> None:
        try:
            while True:
                msg = input("")

                if msg.lower() == 'quit':
                    break

                self.sock.send(msg.encode('utf-8'))

        except Exception as e:
            print(f"Error sending message: {e}")

        finally:
            self.sock.close()



    def run(self) -> None:
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