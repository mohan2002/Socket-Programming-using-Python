import socket

def server():
    IPADDR = socket.gethostbyname(socket.gethostname())
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((IPADDR,8081))
    server.listen()
    serversocket,address = server.accept()
    print("client connected")
    while(True):
        print("Type a message >")
        message = input()
        serversocket.send(message.encode('utf-8'))

        print("----------------------Waiting for reply-----------------------")

        replymessage = serversocket.recv(1024)
        print("Message from client > " + replymessage.decode('utf-8'))
        




def client():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serveraddr = input("Enter server address you want to connect:")
    client.connect((serveraddr,8081))
    print("Client running")
    while(True):
        print("----------------------Waiting for reply-----------------------")
        data = client.recv(1024)
        print("Message from server > " + data.decode('utf-8'))

        print("Type a message >")
        message = input()
        client.send(message.encode('utf-8'))

    





choice = input("Choose Server or Client:")

if choice == "server" or choice == "Server":
    server()
else:
    client()

