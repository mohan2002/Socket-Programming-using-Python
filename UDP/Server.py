import socket

IPADDR = socket.gethostbyname(socket.gethostname())

udpserver = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpserver.bind((IPADDR,8081))

data,address = udpserver.recvfrom(1024)
print(data.decode())

message = "GOT IT BUGGAH".encode('utf-8')
udpserver.sendto(message,address)