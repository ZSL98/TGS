# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trainer_to_scheduler.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='trainer_to_scheduler.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1atrainer_to_scheduler.proto\"R\n\x16RegisterTrainerRequest\x12\x12\n\ntrainer_ip\x18\x01 \x01(\t\x12\x14\n\x0ctrainer_port\x18\x02 \x01(\r\x12\x0e\n\x06job_id\x18\x03 \x01(\r\"*\n\x17RegisterTrainerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"A\n\x12ReportStatsRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\r\x12\x1b\n\x13\x66inished_iterations\x18\x02 \x01(\r\"&\n\x13ReportStatsResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\x98\x01\n\x12TrainerToScheduler\x12\x46\n\x0fRegisterTrainer\x12\x17.RegisterTrainerRequest\x1a\x18.RegisterTrainerResponse\"\x00\x12:\n\x0bReportStats\x12\x13.ReportStatsRequest\x1a\x14.ReportStatsResponse\"\x00\x62\x06proto3'
)




_REGISTERTRAINERREQUEST = _descriptor.Descriptor(
  name='RegisterTrainerRequest',
  full_name='RegisterTrainerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='trainer_ip', full_name='RegisterTrainerRequest.trainer_ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trainer_port', full_name='RegisterTrainerRequest.trainer_port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_id', full_name='RegisterTrainerRequest.job_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=30,
  serialized_end=112,
)


_REGISTERTRAINERRESPONSE = _descriptor.Descriptor(
  name='RegisterTrainerResponse',
  full_name='RegisterTrainerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='RegisterTrainerResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=114,
  serialized_end=156,
)


_REPORTSTATSREQUEST = _descriptor.Descriptor(
  name='ReportStatsRequest',
  full_name='ReportStatsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='ReportStatsRequest.job_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='finished_iterations', full_name='ReportStatsRequest.finished_iterations', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=158,
  serialized_end=223,
)


_REPORTSTATSRESPONSE = _descriptor.Descriptor(
  name='ReportStatsResponse',
  full_name='ReportStatsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='ReportStatsResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=225,
  serialized_end=263,
)

DESCRIPTOR.message_types_by_name['RegisterTrainerRequest'] = _REGISTERTRAINERREQUEST
DESCRIPTOR.message_types_by_name['RegisterTrainerResponse'] = _REGISTERTRAINERRESPONSE
DESCRIPTOR.message_types_by_name['ReportStatsRequest'] = _REPORTSTATSREQUEST
DESCRIPTOR.message_types_by_name['ReportStatsResponse'] = _REPORTSTATSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterTrainerRequest = _reflection.GeneratedProtocolMessageType('RegisterTrainerRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERTRAINERREQUEST,
  '__module__' : 'trainer_to_scheduler_pb2'
  # @@protoc_insertion_point(class_scope:RegisterTrainerRequest)
  })
_sym_db.RegisterMessage(RegisterTrainerRequest)

RegisterTrainerResponse = _reflection.GeneratedProtocolMessageType('RegisterTrainerResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERTRAINERRESPONSE,
  '__module__' : 'trainer_to_scheduler_pb2'
  # @@protoc_insertion_point(class_scope:RegisterTrainerResponse)
  })
_sym_db.RegisterMessage(RegisterTrainerResponse)

ReportStatsRequest = _reflection.GeneratedProtocolMessageType('ReportStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTSTATSREQUEST,
  '__module__' : 'trainer_to_scheduler_pb2'
  # @@protoc_insertion_point(class_scope:ReportStatsRequest)
  })
_sym_db.RegisterMessage(ReportStatsRequest)

ReportStatsResponse = _reflection.GeneratedProtocolMessageType('ReportStatsResponse', (_message.Message,), {
  'DESCRIPTOR' : _REPORTSTATSRESPONSE,
  '__module__' : 'trainer_to_scheduler_pb2'
  # @@protoc_insertion_point(class_scope:ReportStatsResponse)
  })
_sym_db.RegisterMessage(ReportStatsResponse)



_TRAINERTOSCHEDULER = _descriptor.ServiceDescriptor(
  name='TrainerToScheduler',
  full_name='TrainerToScheduler',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=266,
  serialized_end=418,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterTrainer',
    full_name='TrainerToScheduler.RegisterTrainer',
    index=0,
    containing_service=None,
    input_type=_REGISTERTRAINERREQUEST,
    output_type=_REGISTERTRAINERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReportStats',
    full_name='TrainerToScheduler.ReportStats',
    index=1,
    containing_service=None,
    input_type=_REPORTSTATSREQUEST,
    output_type=_REPORTSTATSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRAINERTOSCHEDULER)

DESCRIPTOR.services_by_name['TrainerToScheduler'] = _TRAINERTOSCHEDULER

# @@protoc_insertion_point(module_scope)
