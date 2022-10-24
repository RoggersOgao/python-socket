import socket

s = socket.socket()

print("socket craeted")

# bind the socket with a port number

# You can use any port from the range of 0 to 65535
# as long as the port is not in use
s.bind(('localhost', 9998))

# start listenning to the client


# for me i will be listenning for 2 client others will be rejected
s.listen(2)
print("waiting for connections")

while True:
    # accept the connection which is the client socket and the address
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("connected with ", addr, name)
    c.send(bytes('Yaaaay!!! I love CSCI-434-02W because the course instructor is really awesome ' + name, 'utf-8'))

    c.close()
