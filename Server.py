import socket
s = socket.socket()
print("Socket created")
port = 56988
s.bind(('', port))
s.listen(5)
while True:
    c, addr = s.accept()
    print(addr)
    message = "Thank you for connecting"
    c.send(message.encode())
    c.close()