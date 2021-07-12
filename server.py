import socket
CHUNK = 65535 # recieve at most these bytes of data at once
port = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a socket obj
# socket.socket(family, type)
# AF_INET: family of ipv4 ip address(32 bits)
# SOCK_DGRAM: UDP, SOCK_STREAM: TCP

# some ip address that the server will listen to when message comes

hostname = '127.0.0.1' # ip add local machine, same for everyone
# aka home, there is no place like 127.0.0.1

s.bind((hostname, port)) # bind the socket with the host machine and on port 3000

print(f"server is live on {s.getsockname()}")

# run the server infinitely, till I stop manually
while True:
    data, clientAdd = s.recvfrom(CHUNK)
    message = data.decode('ascii') # data by default travels in bytes
    print(f"Client at {clientAdd} Says: {message}")
    message_send = input("Reply: ")
    data = message_send.encode('ascii')
    # send data to the ip address that sent me the data
    s.sendto(data, clientAdd)
