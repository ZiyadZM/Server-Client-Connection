import socket
s = socket.socket()
print("Socket created")
port = 56788
s.bind(('', port))
print(f"\nsocket binded to port : {port}")
s.listen(5)
print("\nServer is listening for incoming connections")
while True:
    c, addr = s.accept()
    print(addr)
    message = "\nThank you for connecting"
    c_message = c.recv(1024).decode()
    print(f"\nReceived from client: {c_message}")

    response_message = "\nMessage received by the server."
    c.send(response_message.encode())
    c.send(message.encode())
    c.close()