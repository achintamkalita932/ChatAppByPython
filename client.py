import socket
port = 3000
CHUNK = 65535
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a socket object

# instead of explicitly binding the socket, i will let OS do it.
# ephemaral ports
# OS will bind this for us

hostname = '127.0.0.1'
while True:
    s.connect((hostname, port))
    message = input("Type: ")
    data = message.encode('ascii')
    s.send(data)
    # data recieved:
    data = s.recv(CHUNK)
    text = data.decode('ascii')
    print(f"Host Says: {text}")
