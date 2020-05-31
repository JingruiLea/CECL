# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_manager/gen/data_manager.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data_manager/gen/data_manager.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n#data_manager/gen/data_manager.proto\"!\n\nAddTaskReq\x12\x13\n\x04task\x18\x01 \x01(\x0b\x32\x05.Task\"&\n\x0b\x41\x64\x64TaskResp\x12\x17\n\x04resp\x18\x01 \x01(\x0b\x32\t.Response\"3\n\x0cStartTaskReq\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x12\n\nstart_time\x18\x02 \x01(\x03\"(\n\rStartTaskResp\x12\x17\n\x04resp\x18\x01 \x01(\x0b\x32\t.Response\"1\n\x0bStopTaskReq\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x11\n\tstop_time\x18\x02 \x01(\x03\"\'\n\x0cStopTaskResp\x12\x17\n\x04resp\x18\x01 \x01(\x0b\x32\t.Response\"5\n\rFinishTaskReq\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x13\n\x0b\x66inish_time\x18\x02 \x01(\x03\")\n\x0e\x46inishTaskResp\x12\x17\n\x04resp\x18\x01 \x01(\x0b\x32\t.Response\"\x1d\n\nGetTaskReq\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\"&\n\x0bGetTaskResp\x12\x17\n\x04resp\x18\x01 \x01(\x0b\x32\t.Response\"\x10\n\x0eGetAllTasksReq\"*\n\x0fGetAllTasksResp\x12\x17\n\x04resp\x18\x01 \x01(\x0b\x32\t.Response\"$\n\rUpdateTaskReq\x12\x13\n\x04task\x18\x01 \x01(\x0b\x32\x05.Task\")\n\x0eUpdateTaskResp\x12\x17\n\x04resp\x18\x01 \x01(\x0b\x32\t.Response\"\x96\x01\n\x04Task\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x03 \x01(\x03\x12\x12\n\nstart_time\x18\x04 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x05 \x01(\x03\x12\x13\n\x0bunion_train\x18\x06 \x01(\x05\x12\x11\n\tedgenodes\x18\x07 \x01(\t\x12\x0c\n\x04\x66ile\x18\x08 \x01(\t\")\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t2\xcc\x02\n\x0b\x44\x61taManager\x12&\n\x07\x41\x64\x64Task\x12\x0b.AddTaskReq\x1a\x0c.AddTaskResp\"\x00\x12,\n\tStartTask\x12\r.StartTaskReq\x1a\x0e.StartTaskResp\"\x00\x12)\n\x08StopTask\x12\x0c.StopTaskReq\x1a\r.StopTaskResp\"\x00\x12/\n\nFinishTask\x12\x0e.FinishTaskReq\x1a\x0f.FinishTaskResp\"\x00\x12&\n\x07GetTask\x12\x0b.GetTaskReq\x1a\x0c.GetTaskResp\"\x00\x12\x32\n\x0bGetAllTasks\x12\x0f.GetAllTasksReq\x1a\x10.GetAllTasksResp\"\x00\x12/\n\nUpdateTask\x12\x0e.UpdateTaskReq\x1a\x0f.UpdateTaskResp\"\x00\x62\x06proto3'
)




_ADDTASKREQ = _descriptor.Descriptor(
  name='AddTaskReq',
  full_name='AddTaskReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='AddTaskReq.task', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=72,
)


_ADDTASKRESP = _descriptor.Descriptor(
  name='AddTaskResp',
  full_name='AddTaskResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='AddTaskResp.resp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=112,
)


_STARTTASKREQ = _descriptor.Descriptor(
  name='StartTaskReq',
  full_name='StartTaskReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='StartTaskReq.task_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='StartTaskReq.start_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=165,
)


_STARTTASKRESP = _descriptor.Descriptor(
  name='StartTaskResp',
  full_name='StartTaskResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='StartTaskResp.resp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=207,
)


_STOPTASKREQ = _descriptor.Descriptor(
  name='StopTaskReq',
  full_name='StopTaskReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='StopTaskReq.task_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_time', full_name='StopTaskReq.stop_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=258,
)


_STOPTASKRESP = _descriptor.Descriptor(
  name='StopTaskResp',
  full_name='StopTaskResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='StopTaskResp.resp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=260,
  serialized_end=299,
)


_FINISHTASKREQ = _descriptor.Descriptor(
  name='FinishTaskReq',
  full_name='FinishTaskReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='FinishTaskReq.task_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finish_time', full_name='FinishTaskReq.finish_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=301,
  serialized_end=354,
)


_FINISHTASKRESP = _descriptor.Descriptor(
  name='FinishTaskResp',
  full_name='FinishTaskResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='FinishTaskResp.resp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=356,
  serialized_end=397,
)


_GETTASKREQ = _descriptor.Descriptor(
  name='GetTaskReq',
  full_name='GetTaskReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='GetTaskReq.task_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=399,
  serialized_end=428,
)


_GETTASKRESP = _descriptor.Descriptor(
  name='GetTaskResp',
  full_name='GetTaskResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='GetTaskResp.resp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=430,
  serialized_end=468,
)


_GETALLTASKSREQ = _descriptor.Descriptor(
  name='GetAllTasksReq',
  full_name='GetAllTasksReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=470,
  serialized_end=486,
)


_GETALLTASKSRESP = _descriptor.Descriptor(
  name='GetAllTasksResp',
  full_name='GetAllTasksResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='GetAllTasksResp.resp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=488,
  serialized_end=530,
)


_UPDATETASKREQ = _descriptor.Descriptor(
  name='UpdateTaskReq',
  full_name='UpdateTaskReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='UpdateTaskReq.task', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=568,
)


_UPDATETASKRESP = _descriptor.Descriptor(
  name='UpdateTaskResp',
  full_name='UpdateTaskResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='UpdateTaskResp.resp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=570,
  serialized_end=611,
)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='Task.task_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Task.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='Task.create_time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='Task.start_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='Task.end_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='union_train', full_name='Task.union_train', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edgenodes', full_name='Task.edgenodes', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file', full_name='Task.file', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=614,
  serialized_end=764,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='Response.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='Response.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=766,
  serialized_end=807,
)

_ADDTASKREQ.fields_by_name['task'].message_type = _TASK
_ADDTASKRESP.fields_by_name['resp'].message_type = _RESPONSE
_STARTTASKRESP.fields_by_name['resp'].message_type = _RESPONSE
_STOPTASKRESP.fields_by_name['resp'].message_type = _RESPONSE
_FINISHTASKRESP.fields_by_name['resp'].message_type = _RESPONSE
_GETTASKRESP.fields_by_name['resp'].message_type = _RESPONSE
_GETALLTASKSRESP.fields_by_name['resp'].message_type = _RESPONSE
_UPDATETASKREQ.fields_by_name['task'].message_type = _TASK
_UPDATETASKRESP.fields_by_name['resp'].message_type = _RESPONSE
DESCRIPTOR.message_types_by_name['AddTaskReq'] = _ADDTASKREQ
DESCRIPTOR.message_types_by_name['AddTaskResp'] = _ADDTASKRESP
DESCRIPTOR.message_types_by_name['StartTaskReq'] = _STARTTASKREQ
DESCRIPTOR.message_types_by_name['StartTaskResp'] = _STARTTASKRESP
DESCRIPTOR.message_types_by_name['StopTaskReq'] = _STOPTASKREQ
DESCRIPTOR.message_types_by_name['StopTaskResp'] = _STOPTASKRESP
DESCRIPTOR.message_types_by_name['FinishTaskReq'] = _FINISHTASKREQ
DESCRIPTOR.message_types_by_name['FinishTaskResp'] = _FINISHTASKRESP
DESCRIPTOR.message_types_by_name['GetTaskReq'] = _GETTASKREQ
DESCRIPTOR.message_types_by_name['GetTaskResp'] = _GETTASKRESP
DESCRIPTOR.message_types_by_name['GetAllTasksReq'] = _GETALLTASKSREQ
DESCRIPTOR.message_types_by_name['GetAllTasksResp'] = _GETALLTASKSRESP
DESCRIPTOR.message_types_by_name['UpdateTaskReq'] = _UPDATETASKREQ
DESCRIPTOR.message_types_by_name['UpdateTaskResp'] = _UPDATETASKRESP
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddTaskReq = _reflection.GeneratedProtocolMessageType('AddTaskReq', (_message.Message,), {
  'DESCRIPTOR' : _ADDTASKREQ,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:AddTaskReq)
  })
_sym_db.RegisterMessage(AddTaskReq)

AddTaskResp = _reflection.GeneratedProtocolMessageType('AddTaskResp', (_message.Message,), {
  'DESCRIPTOR' : _ADDTASKRESP,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:AddTaskResp)
  })
_sym_db.RegisterMessage(AddTaskResp)

StartTaskReq = _reflection.GeneratedProtocolMessageType('StartTaskReq', (_message.Message,), {
  'DESCRIPTOR' : _STARTTASKREQ,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:StartTaskReq)
  })
_sym_db.RegisterMessage(StartTaskReq)

StartTaskResp = _reflection.GeneratedProtocolMessageType('StartTaskResp', (_message.Message,), {
  'DESCRIPTOR' : _STARTTASKRESP,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:StartTaskResp)
  })
_sym_db.RegisterMessage(StartTaskResp)

StopTaskReq = _reflection.GeneratedProtocolMessageType('StopTaskReq', (_message.Message,), {
  'DESCRIPTOR' : _STOPTASKREQ,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:StopTaskReq)
  })
_sym_db.RegisterMessage(StopTaskReq)

StopTaskResp = _reflection.GeneratedProtocolMessageType('StopTaskResp', (_message.Message,), {
  'DESCRIPTOR' : _STOPTASKRESP,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:StopTaskResp)
  })
_sym_db.RegisterMessage(StopTaskResp)

FinishTaskReq = _reflection.GeneratedProtocolMessageType('FinishTaskReq', (_message.Message,), {
  'DESCRIPTOR' : _FINISHTASKREQ,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:FinishTaskReq)
  })
_sym_db.RegisterMessage(FinishTaskReq)

FinishTaskResp = _reflection.GeneratedProtocolMessageType('FinishTaskResp', (_message.Message,), {
  'DESCRIPTOR' : _FINISHTASKRESP,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:FinishTaskResp)
  })
_sym_db.RegisterMessage(FinishTaskResp)

GetTaskReq = _reflection.GeneratedProtocolMessageType('GetTaskReq', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKREQ,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:GetTaskReq)
  })
_sym_db.RegisterMessage(GetTaskReq)

GetTaskResp = _reflection.GeneratedProtocolMessageType('GetTaskResp', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKRESP,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:GetTaskResp)
  })
_sym_db.RegisterMessage(GetTaskResp)

GetAllTasksReq = _reflection.GeneratedProtocolMessageType('GetAllTasksReq', (_message.Message,), {
  'DESCRIPTOR' : _GETALLTASKSREQ,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:GetAllTasksReq)
  })
_sym_db.RegisterMessage(GetAllTasksReq)

GetAllTasksResp = _reflection.GeneratedProtocolMessageType('GetAllTasksResp', (_message.Message,), {
  'DESCRIPTOR' : _GETALLTASKSRESP,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:GetAllTasksResp)
  })
_sym_db.RegisterMessage(GetAllTasksResp)

UpdateTaskReq = _reflection.GeneratedProtocolMessageType('UpdateTaskReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETASKREQ,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:UpdateTaskReq)
  })
_sym_db.RegisterMessage(UpdateTaskReq)

UpdateTaskResp = _reflection.GeneratedProtocolMessageType('UpdateTaskResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETASKRESP,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:UpdateTaskResp)
  })
_sym_db.RegisterMessage(UpdateTaskResp)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:Task)
  })
_sym_db.RegisterMessage(Task)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'data_manager.gen.data_manager_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)



_DATAMANAGER = _descriptor.ServiceDescriptor(
  name='DataManager',
  full_name='DataManager',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=810,
  serialized_end=1142,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddTask',
    full_name='DataManager.AddTask',
    index=0,
    containing_service=None,
    input_type=_ADDTASKREQ,
    output_type=_ADDTASKRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartTask',
    full_name='DataManager.StartTask',
    index=1,
    containing_service=None,
    input_type=_STARTTASKREQ,
    output_type=_STARTTASKRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopTask',
    full_name='DataManager.StopTask',
    index=2,
    containing_service=None,
    input_type=_STOPTASKREQ,
    output_type=_STOPTASKRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FinishTask',
    full_name='DataManager.FinishTask',
    index=3,
    containing_service=None,
    input_type=_FINISHTASKREQ,
    output_type=_FINISHTASKRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTask',
    full_name='DataManager.GetTask',
    index=4,
    containing_service=None,
    input_type=_GETTASKREQ,
    output_type=_GETTASKRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllTasks',
    full_name='DataManager.GetAllTasks',
    index=5,
    containing_service=None,
    input_type=_GETALLTASKSREQ,
    output_type=_GETALLTASKSRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTask',
    full_name='DataManager.UpdateTask',
    index=6,
    containing_service=None,
    input_type=_UPDATETASKREQ,
    output_type=_UPDATETASKRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATAMANAGER)

DESCRIPTOR.services_by_name['DataManager'] = _DATAMANAGER

# @@protoc_insertion_point(module_scope)
