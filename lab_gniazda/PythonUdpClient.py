import socket;

serverIP = "127.0.0.1"
serverPort = 9008
msg = "żółta gęś"

print('PYTHON UDP CLIENT')

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(msg.encode("utf-8"), (serverIP, serverPort))
except Exception as e:
    print(f"An error occured: {e}")
finally:
    client.close()




