                            Clint_server 
We started with how to get your Local IP
---> Open your terminal then Type "ifconfig" then you will have your IP "192.168,---.---"
---> The port number you can use any port you want but not used port
|
|
|
|

#                            Server Code

import socket  ----> Socket module
s = socket.socket() ----> Socket object
print("Socket created") ----> Noting that the socket created
port = 56988 ----> The port number that I put randomly
s.bind(('', port)) ----> Bind the socket to the specified host and port using s.bind(('', port))
s.listen(5) ----> Use s.listen(5) to set the socket to listening mode 5 connections

while True: ----> Loop to keep the server running forever
    c, addr = s.accept() ----> When a client connects, s.accept() returns a new socket c representing the connection and the address addr of the client
    print(addr)
    message = "Thank you for connecting"
    c.send(message.encode()) ----> Send the message to the client. The encode() method converts the message from a string to bytes which is required for sending over the network
    c.close() ----> Close the client socket c using c.close()


#                            Clint Code

import socket  ----> Socket module
s = socket.socket() ----> Socket object
port = 56988 ----> The port number that I put randomly
s.connect(("192.168.100.147", port)) ----> To start a connection to the server at the IP address and port
print(s.recv(1024)) ----> This line receives up to 1024 bytes of data from the server and print it 
s.close() ----> Close the client socket s using s.close()