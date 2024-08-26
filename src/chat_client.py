from threading import Thread
import grpc
import protos.chat_pb2 as chat_pb2
import protos.chat_pb2_grpc as chat_pb2_grpc

'''
ChatClient 

Provides a CLI that enables users to use chat room functionality. 
Responsible for parsing user input and making the corresponding RPC requests.
'''
class ChatClient():

    def __init__(self, stub):
        self.stub = stub

        #used when user joins a room
        self.chat_mode = False
        self.username = ''
        self.chat_room = ''
    
        #thread for receiving messages
        self.recv_thread = None

    #main program loop
    def run(self):
        print('Welcome to 4300Chat! Type /help for a list of commands')
        while(True):
            if self.chat_mode == False:
                self.parse_cmd(input('> '))
            else:
                self.send_msg(input(''))
            
    #parse input commands and make RPC requests
    def parse_cmd(self, cmd):
        tokens = cmd.strip().lower().split()
        if(len(tokens) > 0):
            if tokens[0] == "/create" and len(tokens) == 2:
                response = self.stub.CreateRoom(chat_pb2.CreateRequest(room_name=tokens[1]))
                print(response.message)
            elif tokens[0] == "/list" and len(tokens) == 1:
                response = self.stub.ListRooms(chat_pb2.ListRequest())
                print(response.message)
            elif tokens[0] == '/info' and len(tokens) == 2:
                response = self.stub.GetRoomInfo(chat_pb2.InfoRequest(room_name=tokens[1]))
                print(response.info)
            elif tokens [0] == "/join" and len(tokens) == 3:
                response = self.stub.JoinRoom(chat_pb2.JoinRequest(room_name=tokens[1], user=tokens[2]))
                print(response.message)
                if response.success:
                    self.chat_mode = True
                    self.chat_room = tokens[1]
                    self.username = tokens[2]

                    #on successful join room, start receiving thread
                    self.recv_thread = Thread(target=self.receive_messages)
                    self.recv_thread.start()
            elif tokens [0] == "/leave" and len(tokens) == 1:
                print("not currently in a room")
            elif tokens[0] == "/help" and len(tokens) == 1:
                print("create room: /create [room name]\n"
                      "list existing rooms: /list\n"
                      "get room info: /info [room name]\n"
                      "join room: /join [room name] [username]\n"
                      "leave room: /leave")
            else:
                print("invalid command format")
        
    #sends a message to the server. if the user inputs the /leave command, leave the room instead
    def send_msg(self, msg):
        if msg.strip().lower() == "/leave":
            response = self.stub.LeaveRoom(chat_pb2.LeaveRequest(room_name=self.chat_room, user=self.username))
            if response.success:
                self.username = ''
                self.chat_room = ''
                self.chat_mode = False
        else:
            self.stub.SendMessage(chat_pb2.SendRequest(room_name=self.chat_room, user=self.username, message=msg))

    #continuously receive and print messages from server. should be called in a seperate thread
    def receive_messages(self):
        chat_messages = self.stub.GetMessages(chat_pb2.GetMessagesRequest(room_name=self.chat_room, user=self.username))
        for m in chat_messages:
            print("[{}]: {}".format(m.user, m.message))

if __name__ == "__main__":
    host = 'localhost'
    port = '50051'
    channel = grpc.insecure_channel('{}:{}'.format(host, port))
    stub = chat_pb2_grpc.ChatStub(channel)

    c = ChatClient(stub)
    c.run()
