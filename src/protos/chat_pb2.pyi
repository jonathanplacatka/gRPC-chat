from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("room_name",)
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    room_name: str
    def __init__(self, room_name: _Optional[str] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class InfoRequest(_message.Message):
    __slots__ = ("room_name",)
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    room_name: str
    def __init__(self, room_name: _Optional[str] = ...) -> None: ...

class InfoResponse(_message.Message):
    __slots__ = ("info",)
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: str
    def __init__(self, info: _Optional[str] = ...) -> None: ...

class JoinRequest(_message.Message):
    __slots__ = ("room_name", "user")
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    room_name: str
    user: str
    def __init__(self, room_name: _Optional[str] = ..., user: _Optional[str] = ...) -> None: ...

class JoinResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class LeaveRequest(_message.Message):
    __slots__ = ("room_name", "user")
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    room_name: str
    user: str
    def __init__(self, room_name: _Optional[str] = ..., user: _Optional[str] = ...) -> None: ...

class LeaveResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class GetMessagesRequest(_message.Message):
    __slots__ = ("room_name", "user")
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    room_name: str
    user: str
    def __init__(self, room_name: _Optional[str] = ..., user: _Optional[str] = ...) -> None: ...

class ChatMessage(_message.Message):
    __slots__ = ("message", "user")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    message: str
    user: str
    def __init__(self, message: _Optional[str] = ..., user: _Optional[str] = ...) -> None: ...

class SendRequest(_message.Message):
    __slots__ = ("room_name", "user", "message")
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    room_name: str
    user: str
    message: str
    def __init__(self, room_name: _Optional[str] = ..., user: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class SendResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
