import socket;

serverIP = "127.0.0.1"
serverPort = 9008
msg = 300

print('PYTHON UDP CLIENT')

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    msg_bytes = (msg).to_bytes(4, byteorder='little')
    client.sendto(msg_bytes, (serverIP, serverPort))
    print(f"Number to server: {msg}")

    data, addr = client.recvfrom(4)
    received_msg = int.from_bytes(data, byteorder='little')
    print(f"Number from server: {received_msg}")

except Exception as e:
    print(f"An error occured: {e}")
finally:
    client.close()




