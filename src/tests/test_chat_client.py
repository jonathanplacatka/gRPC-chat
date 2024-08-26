import unittest
import protos.chat_pb2_grpc as chat_pb2_grpc
from unittest.mock import patch
from chat_client import ChatClient

class TestChatClient(unittest.TestCase):

    #test command parsing - valid commands should cause the corresponding ChatStub methods to be called
    @patch('protos.chat_pb2_grpc.ChatStub')
    def test_parse_create_cmd(self, MockChatStub):
        client = ChatClient(MockChatStub)
        client.parse_cmd('/create')
        MockChatStub.CreateRoom.assert_not_called()
        client.parse_cmd('/create room1')
        MockChatStub.CreateRoom.assert_called()

    @patch('protos.chat_pb2_grpc.ChatStub')
    def test_parse_list_cmd(self, MockChatStub):
        client = ChatClient(MockChatStub)
        client.parse_cmd('/list blah blah')
        MockChatStub.ListRooms.assert_not_called()
        client.parse_cmd('/list')
        MockChatStub.ListRooms.assert_called()

    @patch('protos.chat_pb2_grpc.ChatStub')
    def test_parse_info_cmd(self, MockChatStub):
        client = ChatClient(MockChatStub)
        client.parse_cmd('/info')
        MockChatStub.GetRoomInfo.assert_not_called()
        client.parse_cmd('/info room1')
        MockChatStub.GetRoomInfo.assert_called()

    @patch('protos.chat_pb2_grpc.ChatStub')
    def test_parse_join_cmd(self, MockChatStub):
        client = ChatClient(MockChatStub)
        client.parse_cmd('/join')
        MockChatStub.JoinRoom.assert_not_called()
        client.parse_cmd('/join room1 user1')
        MockChatStub.JoinRoom.assert_called()
        MockChatStub.GetMessages.assert_called()
        self.assertEqual(client.chat_room, 'room1')
        self.assertEqual(client.username, 'user1')
        self.assertTrue(client.chat_mode) 

    @patch('protos.chat_pb2_grpc.ChatStub')
    def test_parse_invalid(self, MockChatStub):
        client = ChatClient(MockChatStub)
        client.parse_cmd('asdf')
        client.parse_cmd('/foo')
        client.parse_cmd('/leave')
        MockChatStub.assert_not_called()

    @patch('protos.chat_pb2_grpc.ChatStub')
    def test_send_msg(self, MockChatStub):
        client = ChatClient(MockChatStub)
        client.parse_cmd('/join room1 user1')
        client.send_msg('hello')
        MockChatStub.SendMessage.assert_called()
    
    @patch('protos.chat_pb2_grpc.ChatStub')
    def test_send_msg_leave(self, MockChatStub):
        client = ChatClient(MockChatStub)
        client.parse_cmd('/join room1 user1')
        client.send_msg('/leave')
        MockChatStub.LeaveRoom.assert_called()

if __name__ == '__main__':
    unittest.main()