import socket

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
message = "Hey mohan".encode('utf-8')
clientsocket.sendto(message,("192.168.43.246",8081))

data,addr = clientsocket.recvfrom(1024)

print(data.decode())