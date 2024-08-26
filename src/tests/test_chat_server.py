import unittest
import protos.chat_pb2 as chat_pb2;

from chat_server import ChatService
from chat_room import ChatRoom

class TestChatServer(unittest.TestCase):

    def test_create_room_success(self):
        service = ChatService()
        request = chat_pb2.CreateRequest(room_name='foo')
        response = service.CreateRoom(request, None)
        self.assertEqual(response.message, 'created room [foo]')
    
    def test_create_room_duplicate(self):
        service = ChatService()
        service.rooms['foo'] = ChatRoom()
        request = chat_pb2.CreateRequest(room_name='foo')
        response = service.CreateRoom(request, None)
        self.assertEqual(response.message, 'cannot create room with duplicate name [foo]')

    def test_list_room_success(self):
         service = ChatService()
         service.rooms['one'] = ChatRoom()
         service.rooms['two'] = ChatRoom()
         service.rooms['three'] = ChatRoom()
         expected = 'one\ntwo\nthree'
         request = chat_pb2.ListRequest()
         response = service.ListRooms(request, None)
         self.assertEqual(response.message, expected)
    
    def test_list_room_empty(self):
         service = ChatService()
         request = chat_pb2.ListRequest()
         response = service.ListRooms(request, None)
         self.assertEqual(response.message, 'no rooms have been created')

    def test_get_room_info_success(self):
        service = ChatService()
        room = ChatRoom()
        room.join('user1')
        room.join('user2')
        service.rooms['foo'] = room
        expected = 'connected users: 2/5\nuser list:\nuser1\nuser2'
        request = chat_pb2.InfoRequest(room_name='foo')
        response = service.GetRoomInfo(request, None)
        self.assertEqual(response.info, expected)
    
    def test_get_room_info_empty(self):
        service = ChatService()
        service.rooms['foo'] = ChatRoom()
        expected = 'connected users: 0/5'
        request = chat_pb2.InfoRequest(room_name='foo')
        response = service.GetRoomInfo(request, None)
        self.assertEqual(response.info, expected)

    def test_get_room_info_not_exists(self):
        service = ChatService()
        request = chat_pb2.InfoRequest(room_name='foo')
        response = service.GetRoomInfo(request, None)
        self.assertEqual(response.info, 'room [foo] does not exist')

    def test_join_room_success(self):
        service = ChatService()
        room = ChatRoom()
        room.join('user1')
        room.join('user2')
        service.rooms['foo'] = room
        request = chat_pb2.JoinRequest(room_name='foo', user='user3')
        response = service.JoinRoom(request, None)
        self.assertTrue(response.success)
        self.assertEqual(response.message, 'joined room [foo]')
        self.assertTrue(room.user_exists('user3'))

    def test_join_room_full(self):
        service = ChatService()
        room = ChatRoom()
        room.join('user1')
        room.join('user2')
        room.join('user3')
        room.join('user4')
        room.join('user5')
        service.rooms['foo'] = room
        request = chat_pb2.JoinRequest(room_name='foo', user='user6')
        response = service.JoinRoom(request, None)
        self.assertFalse(response.success)
        self.assertEqual(response.message, 'room [foo] is full')
        self.assertFalse(room.user_exists('user6'))

    def test_join_room_duplicate_user(self):
        service = ChatService()
        room = ChatRoom()
        room.join('user1')
        service.rooms['foo'] = room
        request = chat_pb2.JoinRequest(room_name='foo', user='user1')
        response = service.JoinRoom(request, None)
        self.assertFalse(response.success)
        self.assertEqual(response.message, 'duplicate username [user1] - choose another username')

    def test_join_room_not_exists(self):
        service = ChatService()
        request = chat_pb2.JoinRequest(room_name='foo', user='user1')
        response = service.JoinRoom(request, None)
        self.assertFalse(response.success)
        self.assertEqual(response.message, 'room [foo] does not exist')
     
    def test_leave_room_success(self):
        service = ChatService()
        room = ChatRoom()
        room.join('user1')
        service.rooms['foo'] = room
        request = chat_pb2.LeaveRequest(room_name='foo', user='user1')
        response = service.LeaveRoom(request, None)
        self.assertTrue(response.success)

    def test_leave_room_not_exists(self):
        service = ChatService()
        request = chat_pb2.LeaveRequest(room_name='foo', user='user1')
        response = service.LeaveRoom(request, None)
        self.assertFalse(response.success)

    def test_leave_room_user_not_exists(self):
        service = ChatService()
        service.rooms['foo'] = ChatRoom()
        request = chat_pb2.LeaveRequest(room_name='foo', user='user1')
        response = service.LeaveRoom(request, None)
        self.assertFalse(response.success)

    def test_get_messages_success(self):
        service = ChatService()
        room = ChatRoom()
        room.join('user1')
        service.rooms['foo'] = room
        room.get_user_queue('user1').put('testmsg') #add message to receive
        request = chat_pb2.GetMessagesRequest(room_name='foo', user='user1')
        messages = service.GetMessages(request, None)
        self.assertEqual(next(messages, None), 'testmsg')

    def test_get_messages_room_not_exists(self):
        service = ChatService()
        request = chat_pb2.GetMessagesRequest(room_name='foo', user='user1')
        messages = service.GetMessages(request, None)
        self.assertIsNone(next(messages, None)) #iterator should have no values

    def test_get_messages_user_not_exists(self):
        service = ChatService()
        service.rooms['foo'] = ChatRoom()
        request = chat_pb2.GetMessagesRequest(room_name='foo', user='user1')
        messages = service.GetMessages(request, None)
        self.assertIsNone(next(messages, None)) #iterator should have no values
    
    def test_send_message_success(self):
        service = ChatService()
        room = ChatRoom()
        room.join('user1')
        service.rooms['foo'] = room
        request = chat_pb2.SendRequest(room_name='foo', user='user1', message='testmsg')
        response = service.SendMessage(request, None)
        self.assertTrue(response.success)
        #check that message is put in queue
        chat_message = room.get_user_queue('user1').get()
        self.assertEqual(chat_message.message, 'testmsg')
        self.assertEqual(chat_message.user, 'user1')

    def test_send_message_room_not_exists(self):
        service = ChatService()
        request = chat_pb2.SendRequest(room_name='foo', user='user1', message='testmsg')
        response = service.SendMessage(request, None)
        self.assertFalse(response.success)

    def test_send_message_user_not_exists(self):
        service = ChatService()
        room = ChatRoom()
        room.join('user1')
        service.rooms['foo'] = room
        request = chat_pb2.SendRequest(room_name='foo', user='user2', message='testmsg')
        response = service.SendMessage(request, None)
        self.assertFalse(response.success)
        #check that message is not put in queue
        self.assertTrue(room.get_user_queue('user1').empty())
   
if __name__ == '__main__':
    unittest.main()