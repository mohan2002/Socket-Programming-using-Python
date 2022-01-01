import socket
import time
from platform import node,python_version_tuple
import pickle

current_time =time.strftime("%H:%M:%S", time.localtime()) 
networkname = node()
pythonversion = python_version_tuple()

message = (current_time,networkname,pythonversion)

data = pickle.dumps(message)


print(current_time,networkname,pythonversion)

udpclient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udpclient.sendto(data,("192.168.43.246",8081))

reply,address = udpclient.recvfrom(1024)
print(reply.decode())

udpclient.close()