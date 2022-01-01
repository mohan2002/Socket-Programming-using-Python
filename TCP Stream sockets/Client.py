import socket

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(("192.168.43.246",8081))

def get_text(clientsocket):
    buffer = ""

    socket_open = True
    while socket_open:
        data = clientsocket.recv(1024)

        if not data:
            socket_open = False
        
        buffer = buffer + data.decode()

        terminate_pos = buffer.find("\n")

        while terminate_pos  > -1:
            message = buffer[:terminate_pos]
            buffer = buffer[terminate_pos+1:]

            yield message

            terminate_pos = buffer.find('\n')

print("Connect to the server")


# if(data != ""):
#     clientmessage = "Bro got a message".encode("utf-8")
#     clientsocket.send(clientmessage)

for message in get_text(clientsocket):
    print(message)


clientsocket.close()