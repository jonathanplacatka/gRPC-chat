from concurrent import futures
import grpc
import protos.chat_pb2_grpc as chat_pb2_grpc;
import protos.chat_pb2 as chat_pb2;
from chat_room import ChatRoom

'''
ChatService

Handles RPC requests from chat clients
'''
class ChatService(chat_pb2_grpc.ChatServicer):

    def __init__(self):
        self.rooms = {} #list of ChatRooms

    #create room if duplicate room name does not exist
    def CreateRoom(self, request, context):
        message="cannot create room with duplicate name [{}]"
        if request.room_name not in self.rooms:
            self.rooms[request.room_name] = ChatRoom()
            message = "created room [{}]"
        return chat_pb2.CreateResponse(message=message.format(request.room_name))
    
    #return list of all rooms, or a message indicating that no rooms exist
    def ListRooms(self, request, context):
        message = 'no rooms have been created'
        if len(self.rooms) >= 1:
            message = ''.join([k + '\n' for k in self.rooms.keys()]).strip('\n')
        return chat_pb2.ListResponse(message=message)
    
    #return number of users in a given room, and a list of users if room is not empty
    def GetRoomInfo(self, request, context):
        message = "room [{}] does not exist".format(request.room_name)
        if room := self.rooms.get(request.room_name):
            message = "connected users: {}/{}".format(room.num_users(), ChatRoom.MAX_CAPACITY)
            if(room.num_users() > 0):
                message += "\nuser list:\n{}".format(room.user_list())
        return chat_pb2.InfoResponse(info=message)
    
    #join a given room. duplicate usernames are not allowed
    def JoinRoom(self, request, context):
        message = "room [{}] does not exist"
        success = False

        if room := self.rooms.get(request.room_name):
            if success := room.join(request.user):
                message = "joined room [{}]"
            elif room.num_users() >= ChatRoom.MAX_CAPACITY:
                message = "room [{}] is full"
            else:
                 message = "duplicate username [{}] - choose another username".format(request.user)      
                
        return chat_pb2.JoinResponse(message=message.format(request.room_name), success=success)
    
    #remove a user from a given room
    def LeaveRoom(self, request, context):
        success = False
        if room := self.rooms.get(request.room_name):
            success = room.leave(request.user)
        return chat_pb2.LeaveResponse(success=success)
    
    #return stream of messages that a client can read from
    def GetMessages(self, request, context): 
        if room := self.rooms.get(request.room_name):
            queue = room.get_user_queue(request.user)
            #add new messages to stream until client leaves room
            while room.user_exists(request.user): 
                yield queue.get()
                
    #send a message to all users in a given room
    def SendMessage(self, request, context):
        success = False
        if room := self.rooms.get(request.room_name):
            if room.user_exists(request.user):
                #send message to all users in room
                room.send_message(chat_pb2.ChatMessage(message=request.message, user=request.user))
                success = True
        return chat_pb2.SendResponse(success=success)
    
def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServicer_to_server(ChatService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == "__main__":
    serve()