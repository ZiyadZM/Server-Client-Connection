import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 56788
s.connect(("192.168.100.147", port))

client_message = "Hello, server!"
s.send(client_message.encode())

server_response = s.recv(1024).decode()
print(f"\nReceived from server: {server_response}")
print(s.recv(1024))
s.close()