from pathlib import PosixPath
import pickle
import socket
from fl_networking_tools import ImageViewer

viewer = ImageViewer()
IPADDR = socket.gethostbyname(socket.gethostname())
udpserver = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpserver.bind((IPADDR,8081))
def printImage():
    lost_pixels = 0
    last_updated_pixel = (-1,-1)
    viewer.text = lost_pixels
    while True:
        data,clientaddr=udpserver.recvfrom(1024)
        message = pickle.loads(data)
        pos,rgba = message[0],message[1]
        viewer.put_pixel(pos,rgba)
        if(pos[0]-last_updated_pixel[0] > 1) or (pos[1]-last_updated_pixel[1] > 1):
            lost_pixels += 1
            viewer.text = lost_pixels
        last_updated_pixel = pos


viewer.start(printImage)

udpserver.close()

