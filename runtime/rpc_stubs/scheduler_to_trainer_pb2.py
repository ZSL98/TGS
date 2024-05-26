# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scheduler_to_trainer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='scheduler_to_trainer.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1ascheduler_to_trainer.proto\"\x13\n\x11QueryStatsRequest\"1\n\x12QueryStatsResponse\x12\x1b\n\x13\x66inished_iterations\x18\x01 \x01(\r2M\n\x12SchedulerToTrainer\x12\x37\n\nQueryStats\x12\x12.QueryStatsRequest\x1a\x13.QueryStatsResponse\"\x00\x62\x06proto3'
)




_QUERYSTATSREQUEST = _descriptor.Descriptor(
  name='QueryStatsRequest',
  full_name='QueryStatsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=30,
  serialized_end=49,
)


_QUERYSTATSRESPONSE = _descriptor.Descriptor(
  name='QueryStatsResponse',
  full_name='QueryStatsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='finished_iterations', full_name='QueryStatsResponse.finished_iterations', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=51,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['QueryStatsRequest'] = _QUERYSTATSREQUEST
DESCRIPTOR.message_types_by_name['QueryStatsResponse'] = _QUERYSTATSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryStatsRequest = _reflection.GeneratedProtocolMessageType('QueryStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSTATSREQUEST,
  '__module__' : 'scheduler_to_trainer_pb2'
  # @@protoc_insertion_point(class_scope:QueryStatsRequest)
  })
_sym_db.RegisterMessage(QueryStatsRequest)

QueryStatsResponse = _reflection.GeneratedProtocolMessageType('QueryStatsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSTATSRESPONSE,
  '__module__' : 'scheduler_to_trainer_pb2'
  # @@protoc_insertion_point(class_scope:QueryStatsResponse)
  })
_sym_db.RegisterMessage(QueryStatsResponse)



_SCHEDULERTOTRAINER = _descriptor.ServiceDescriptor(
  name='SchedulerToTrainer',
  full_name='SchedulerToTrainer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=102,
  serialized_end=179,
  methods=[
  _descriptor.MethodDescriptor(
    name='QueryStats',
    full_name='SchedulerToTrainer.QueryStats',
    index=0,
    containing_service=None,
    input_type=_QUERYSTATSREQUEST,
    output_type=_QUERYSTATSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCHEDULERTOTRAINER)

DESCRIPTOR.services_by_name['SchedulerToTrainer'] = _SCHEDULERTOTRAINER

# @@protoc_insertion_point(module_scope)
