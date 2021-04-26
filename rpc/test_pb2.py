# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc/test.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rpc/test.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0erpc/test.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"N\n\x0bTestRequest\x12\x13\n\x0btest_string\x18\x01 \x01(\t\x12*\n\ttest_dict\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"A\n\x0cTestResponse\x12\x13\n\x0btest_string\x18\x01 \x01(\t\x12\x1c\n\ttest_enum\x18\x02 \x01(\x0e\x32\t.TestEnum*(\n\x08TestEnum\x12\x07\n\x03OP1\x10\x00\x12\n\n\x06OTRAOP\x10\x01\x12\x07\n\x03\x45TC\x10\x02\x32t\n\x0bTestService\x12)\n\x08TestCall\x12\x0c.TestRequest\x1a\r.TestResponse\"\x00\x12:\n\x0fTestCallNoParam\x12\x16.google.protobuf.Empty\x1a\r.TestResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])

_TESTENUM = _descriptor.EnumDescriptor(
  name='TestEnum',
  full_name='TestEnum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OP1', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OTRAOP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ETC', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=224,
  serialized_end=264,
)
_sym_db.RegisterEnumDescriptor(_TESTENUM)

TestEnum = enum_type_wrapper.EnumTypeWrapper(_TESTENUM)
OP1 = 0
OTRAOP = 1
ETC = 2



_TESTREQUEST = _descriptor.Descriptor(
  name='TestRequest',
  full_name='TestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_string', full_name='TestRequest.test_string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_dict', full_name='TestRequest.test_dict', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=77,
  serialized_end=155,
)


_TESTRESPONSE = _descriptor.Descriptor(
  name='TestResponse',
  full_name='TestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_string', full_name='TestResponse.test_string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_enum', full_name='TestResponse.test_enum', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=157,
  serialized_end=222,
)

_TESTREQUEST.fields_by_name['test_dict'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TESTRESPONSE.fields_by_name['test_enum'].enum_type = _TESTENUM
DESCRIPTOR.message_types_by_name['TestRequest'] = _TESTREQUEST
DESCRIPTOR.message_types_by_name['TestResponse'] = _TESTRESPONSE
DESCRIPTOR.enum_types_by_name['TestEnum'] = _TESTENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestRequest = _reflection.GeneratedProtocolMessageType('TestRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTREQUEST,
  '__module__' : 'rpc.test_pb2'
  # @@protoc_insertion_point(class_scope:TestRequest)
  })
_sym_db.RegisterMessage(TestRequest)

TestResponse = _reflection.GeneratedProtocolMessageType('TestResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTRESPONSE,
  '__module__' : 'rpc.test_pb2'
  # @@protoc_insertion_point(class_scope:TestResponse)
  })
_sym_db.RegisterMessage(TestResponse)



_TESTSERVICE = _descriptor.ServiceDescriptor(
  name='TestService',
  full_name='TestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=266,
  serialized_end=382,
  methods=[
  _descriptor.MethodDescriptor(
    name='TestCall',
    full_name='TestService.TestCall',
    index=0,
    containing_service=None,
    input_type=_TESTREQUEST,
    output_type=_TESTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TestCallNoParam',
    full_name='TestService.TestCallNoParam',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_TESTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name['TestService'] = _TESTSERVICE

# @@protoc_insertion_point(module_scope)