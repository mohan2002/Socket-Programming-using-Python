# The socket server library is a more powerful module for handling sockets, it will help you set up and manage multiple clients in the next step
import socketserver
from collections import namedtuple
from fl_networking_tools import get_binary, send_binary
from time import sleep
from threading import Event
from random import choice


'''
Commands:
PLACE YOUR COMMANDS HERE
QUES - question command
'''

NUMBER_OF_PLAYERS = 2
players = []
readytostart = Event()



class ThreadedTCPServer(socketserver.ThreadingMixIn,socketserver.TCPServer):
    pass

# Named tuples are extensions of the tuple structure, with contents you can refer to by name. In this case, the question will be held in a variable named q and the answer in answer.
# This is just the set up of the question - it will be sent to the client using the send_binary function when a request is made.
Question = namedtuple('Question', ['q', 'answer'])

q1 = Question("Expand the acronym ALU", "Arithmetic Logic Unit")

quiz_questions = [
    Question("Expand the acronym ALU", "Arithmetic Logic Unit"),
    Question("What does RAM stand for?", "Random Access Memory")
]
# The socketserver module uses 'Handlers' to interact with connections. When a client connects a version of this class is made to handle it.
class QuizGame(socketserver.BaseRequestHandler):
    # The handle method is what actually handles the connection
    def handle(self):
        #Retrieve Command
        for command in get_binary(self.request):
            if command[0] == "JOIN":
                players.append(command[1])
                if len(players) == NUMBER_OF_PLAYERS:
                    # If correct number of players
                    readytostart.set()
                    # Trigger the event
                else:
                    send_binary(self.request,[4,"Wait for other players to join"])

                # Send the confirmation response
                send_binary(self.request, [2, ""])
                # Wait for the ready to start event
                readytostart.wait()
            
            elif command[0] == "READY":
                #Send question
                current_qn = choice(quiz_questions)
                send_binary(self.request, (1, current_qn.q))
            elif command[0] == "ANS":
                print("Ans Recieved")
                sleep(1)
                ans = command[1]
                if(ans == current_qn.answer):
                    send_binary(self.request,(3,"Correct Ans"))
                    if current_qn in quiz_questions:
                        quiz_questions.remove(current_qn)
                else:
                    send_binary(self.request,(3,"Wrong Ans"))

                
                

            
        #Your server code goes here


# Open the quiz server and bind it to a port - creating a socket
# This works similarly to the sockets you used before, but you have to give it both an address pair (IP and port) and a handler for the server.

quiz_server = ThreadedTCPServer(('127.0.0.1', 2065), QuizGame)
quiz_server.serve_forever()
