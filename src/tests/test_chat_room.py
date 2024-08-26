import unittest
import protos.chat_pb2 as chat_pb2;

from chat_room import ChatRoom

class TestChatRoom(unittest.TestCase):

    def test_num_users(self):
        room = ChatRoom()
        self.assertEqual(room.num_users(), 0)
        room.join('user1')
        self.assertEqual(room.num_users(), 1)
        room.join('user2')
        room.join('user3')
        self.assertEqual(room.num_users(), 3)

    def test_user_list(self):
        room = ChatRoom()
        
        #get empty list
        self.assertEqual(room.user_list(), '') 

        room.join('user1') 
        room.join('user2')
        room.join('user3')

        self.assertEqual(room.user_list(), 'user1\nuser2\nuser3')

    def test_join(self):
        room = ChatRoom()
        self.assertTrue(room.join('user1')) 

        #join with duplicate username
        self.assertFalse(room.join('user1')) 

        self.assertTrue(room.join('user2'))
        self.assertTrue(room.join('user3'))
        self.assertTrue(room.join('user4'))
        self.assertTrue(room.join('user5'))

        #join full room
        self.assertFalse(room.join('user6')) 

    def test_leave(self):
        room = ChatRoom()
        room.join('user1')
        self.assertTrue(room.leave('user1'))
        self.assertEqual(room.num_users(), 0)

        #user does not exist
        self.assertFalse(room.leave('user2')) 

    def test_get_user_queue(self):
        room = ChatRoom()
        room.join('user1')
        self.assertIsNotNone(room.get_user_queue('user1'))

        #user does not exist
        self.assertIsNone(room.get_user_queue('user2')) 

    def test_user_exists(self):
        room = ChatRoom()
        room.join('user1')
        self.assertTrue(room.user_exists('user1'))
        self.assertFalse(room.user_exists('user2'))

    def test_send_message(self):
        room = ChatRoom()
        room.join('user1')
        room.join('user2')

        m = chat_pb2.ChatMessage(message='testmsg', user='user1')
        room.send_message(m)

        #check that message is put in both users' message queues
        q1 = room.get_user_queue('user1')
        m1 = q1.get()
        self.assertEqual(m1.user, 'user1')
        self.assertEqual(m1.message, 'testmsg')

        q2 = room.get_user_queue('user2')
        m2 = q2.get()
        self.assertEqual(m2.user, 'user1')
        self.assertEqual(m2.message, 'testmsg')

if __name__ == '__main__':
    unittest.main()