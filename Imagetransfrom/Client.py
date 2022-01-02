from PIL import Image
import socket
import pickle
from random import randint

pixels_lost = 0 

udpclient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
image = Image.open("./rasperby.jpg")
width,height = image.size

for y in range(height):
    for x in range(width):
        pos  = (x,y)
        rgba = image.getpixel(pos)
        message = (pos,rgba)
        data = pickle.dumps(message)
        
        if randint(0,9) > 0:
            udpclient.sendto(data,("192.168.43.246",8081))
        else:
            pixels_lost += 1

print("Image sent")
print(pixels_lost)