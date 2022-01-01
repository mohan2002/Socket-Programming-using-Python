import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_addr = socket.gethostbyname(socket.gethostname())
server.bind((server_addr,8081))
server.listen()
print("Server listening",server_addr)

def send_text(conn_socket,text):
    text = text+'\n'
    datas =  text.encode()
    conn_socket.send(datas)

conn_socket,address = server.accept()
print("Yay connection successful")

message = "Hello, thanks for connecting\nHey buddy \nHai how are you"

data = message.encode('utf-8')
send_text(conn_socket,message)

print("Message sent")

# servermessage = conn_socket.recv(1024)
# print(servermessage.decode('utf-8'))

server.close()
conn_socket.close()
