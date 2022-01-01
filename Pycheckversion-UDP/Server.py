import socket
import pickle

IPADDR = socket.gethostbyname(socket.gethostname())
udpserver = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpserver.bind((IPADDR,8081))
print("Connection waiting")

data,address = udpserver.recvfrom(1024)

message = pickle.loads(data)

latest_pythonv = ('3','10','1')
print(message[0])
print(message[1])
print(message[2])
if(message[2] != latest_pythonv):
    mess = "Your machine is not latest version upgrade to the LTS version"
    udpserver.sendto(mess.encode('utf-8'),address)

udpserver.close()
