import socket
s = socket.socket()
port = 56988
s.connect(("192.168.100.147", port))
print(s.recv(1024))
s.close()