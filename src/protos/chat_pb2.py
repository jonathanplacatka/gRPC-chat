# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/chat.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11protos/chat.proto\"\"\n\rCreateRequest\x12\x11\n\troom_name\x18\x01 \x02(\t\"!\n\x0e\x43reateResponse\x12\x0f\n\x07message\x18\x01 \x02(\t\"\r\n\x0bListRequest\"\x1f\n\x0cListResponse\x12\x0f\n\x07message\x18\x01 \x02(\t\" \n\x0bInfoRequest\x12\x11\n\troom_name\x18\x01 \x02(\t\"\x1c\n\x0cInfoResponse\x12\x0c\n\x04info\x18\x01 \x02(\t\".\n\x0bJoinRequest\x12\x11\n\troom_name\x18\x01 \x02(\t\x12\x0c\n\x04user\x18\x02 \x02(\t\"0\n\x0cJoinResponse\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x03 \x02(\t\"/\n\x0cLeaveRequest\x12\x11\n\troom_name\x18\x01 \x02(\t\x12\x0c\n\x04user\x18\x02 \x02(\t\" \n\rLeaveResponse\x12\x0f\n\x07success\x18\x01 \x02(\x08\"5\n\x12GetMessagesRequest\x12\x11\n\troom_name\x18\x01 \x02(\t\x12\x0c\n\x04user\x18\x02 \x02(\t\",\n\x0b\x43hatMessage\x12\x0f\n\x07message\x18\x01 \x02(\t\x12\x0c\n\x04user\x18\x02 \x02(\t\"?\n\x0bSendRequest\x12\x11\n\troom_name\x18\x01 \x02(\t\x12\x0c\n\x04user\x18\x02 \x02(\t\x12\x0f\n\x07message\x18\x03 \x02(\t\"\x1f\n\x0cSendResponse\x12\x0f\n\x07success\x18\x01 \x02(\x08\x32\xc0\x02\n\x04\x43hat\x12-\n\nCreateRoom\x12\x0e.CreateRequest\x1a\x0f.CreateResponse\x12(\n\tListRooms\x12\x0c.ListRequest\x1a\r.ListResponse\x12*\n\x0bGetRoomInfo\x12\x0c.InfoRequest\x1a\r.InfoResponse\x12\'\n\x08JoinRoom\x12\x0c.JoinRequest\x1a\r.JoinResponse\x12*\n\tLeaveRoom\x12\r.LeaveRequest\x1a\x0e.LeaveResponse\x12\x32\n\x0bGetMessages\x12\x13.GetMessagesRequest\x1a\x0c.ChatMessage0\x01\x12*\n\x0bSendMessage\x12\x0c.SendRequest\x1a\r.SendResponse')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.chat_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CREATEREQUEST']._serialized_start=21
  _globals['_CREATEREQUEST']._serialized_end=55
  _globals['_CREATERESPONSE']._serialized_start=57
  _globals['_CREATERESPONSE']._serialized_end=90
  _globals['_LISTREQUEST']._serialized_start=92
  _globals['_LISTREQUEST']._serialized_end=105
  _globals['_LISTRESPONSE']._serialized_start=107
  _globals['_LISTRESPONSE']._serialized_end=138
  _globals['_INFOREQUEST']._serialized_start=140
  _globals['_INFOREQUEST']._serialized_end=172
  _globals['_INFORESPONSE']._serialized_start=174
  _globals['_INFORESPONSE']._serialized_end=202
  _globals['_JOINREQUEST']._serialized_start=204
  _globals['_JOINREQUEST']._serialized_end=250
  _globals['_JOINRESPONSE']._serialized_start=252
  _globals['_JOINRESPONSE']._serialized_end=300
  _globals['_LEAVEREQUEST']._serialized_start=302
  _globals['_LEAVEREQUEST']._serialized_end=349
  _globals['_LEAVERESPONSE']._serialized_start=351
  _globals['_LEAVERESPONSE']._serialized_end=383
  _globals['_GETMESSAGESREQUEST']._serialized_start=385
  _globals['_GETMESSAGESREQUEST']._serialized_end=438
  _globals['_CHATMESSAGE']._serialized_start=440
  _globals['_CHATMESSAGE']._serialized_end=484
  _globals['_SENDREQUEST']._serialized_start=486
  _globals['_SENDREQUEST']._serialized_end=549
  _globals['_SENDRESPONSE']._serialized_start=551
  _globals['_SENDRESPONSE']._serialized_end=582
  _globals['_CHAT']._serialized_start=585
  _globals['_CHAT']._serialized_end=905
# @@protoc_insertion_point(module_scope)
