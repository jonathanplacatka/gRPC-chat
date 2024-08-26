from queue import Queue

'''
ChatRoom

Provides chatroom-related functionality
'''
class ChatRoom:

    MAX_CAPACITY = 5 #max number of users allowed in a single room

    def __init__(self):
        #stores users in the chat room. key = username, value = message queue for user
        self._users = {} 

    #returns number of users currently in the chatroom
    def num_users(self):
        return len(self._users)
    
    #return string list of users
    def user_list(self):
        return ''.join([k + '\n' for k in self._users.keys()]).strip('\n')
    
    #try to add a new user to the chatroom. returns boolean indicating success
    #duplicate usernames are not allowed
    def join(self, username):
        if len(self._users) < ChatRoom.MAX_CAPACITY and not self.user_exists(username):
            self._users[username] = Queue()
            return True
        else:
            return False
        
    #try to remove a user from the chatroom. returns boolean indicating success
    def leave(self, username):
        if username in self._users.keys():
            del self._users[username]
            return True
        else:
            return False

    #given a username, return the corresponding message queue - used to stream messages to the user
    def get_user_queue(self, username):
        return self._users.get(username)
    
    #check if a given user is in the chat room
    def user_exists(self, username):
        return username in self._users
        
    #add a message to all users' message queues
    def send_message(self, chat_message):
        for q in self._users.values():
            q.put(chat_message)
        
