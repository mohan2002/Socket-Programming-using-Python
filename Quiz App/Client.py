import socket
# Import the functions from the networking tools module
from fl_networking_tools import get_binary, send_binary

'''
Responses
LIST YOUR RESPONSE CODES HERE
1 - Question
'''

# A flag used to control the quiz loop.
playing = True

teamname = input("Enter your team name:")
Ipaddress = input("Enter the server you want to connect:")

quiz_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

quiz_server.connect((Ipaddress, 2065))

# Sending a command to the server.
send_binary(quiz_server, ["JOIN", teamname])

while playing:
    # The get_binary function returns a list of messages - loop over them
    for response in get_binary(quiz_server):
        # response is the command/response tuple - response[0] is the code
        if response[0] == 1: # The question response
            # Display it to the user.
            print(response[1])
            answer = input("Enter your answer >")
            send_binary(quiz_server,["ANS",answer])
        elif response[0] == 2:
            send_binary(quiz_server,["READY"])
        elif response[0] == 3:
            print(response[1])
            send_binary(quiz_server,["READY"])
        elif response[0] == 4:
            print(response[1])
        elif response[0] == 5:
            print(response[1])