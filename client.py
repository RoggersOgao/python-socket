import socket

c = socket.socket()

c.connect(('localhost', 9998))


# ask the user for the name

name = input("Enter your name: ")

# send the name to the server
c.send(bytes(name, 'utf-8'))
# print whatever you receive from the server

print(c.recv(1024).decode())