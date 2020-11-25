# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nuance/nlu/v1/single-intent-interpretation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nuance.nlu.v1 import interpretation_common_pb2 as nuance_dot_nlu_dot_v1_dot_interpretation__common__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nuance/nlu/v1/single-intent-interpretation.proto',
  package='nuance.nlu.v1',
  syntax='proto3',
  serialized_options=b'\n\025com.nuance.rpc.nlu.v1B\037SingleIntentInterpretationProtoP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0nuance/nlu/v1/single-intent-interpretation.proto\x12\rnuance.nlu.v1\x1a)nuance/nlu/v1/interpretation-common.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x8e\x02\n\x1aSingleIntentInterpretation\x12\x0e\n\x06intent\x18\x02 \x01(\t\x12\x12\n\nconfidence\x18\x03 \x01(\x02\x12)\n\x06origin\x18\x04 \x01(\x0e\x32\x19.nuance.nlu.v1.EnumOrigin\x12I\n\x08\x65ntities\x18\x05 \x03(\x0b\x32\x37.nuance.nlu.v1.SingleIntentInterpretation.EntitiesEntry\x1aV\n\rEntitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.nuance.nlu.v1.SingleIntentEntityList:\x02\x38\x01\"M\n\x16SingleIntentEntityList\x12\x33\n\x08\x65ntities\x18\x01 \x03(\x0b\x32!.nuance.nlu.v1.SingleIntentEntity\"\xb5\x03\n\x12SingleIntentEntity\x12,\n\ntext_range\x18\x01 \x01(\x0b\x32\x18.nuance.nlu.v1.TextRange\x12\x12\n\nconfidence\x18\x03 \x01(\x02\x12)\n\x06origin\x18\x04 \x01(\x0e\x32\x19.nuance.nlu.v1.EnumOrigin\x12\x41\n\x08\x65ntities\x18\x05 \x03(\x0b\x32/.nuance.nlu.v1.SingleIntentEntity.EntitiesEntry\x12\x16\n\x0cstring_value\x18\x06 \x01(\tH\x00\x12/\n\x0cstruct_value\x18\x07 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x12\x0f\n\x07literal\x18\x08 \x01(\t\x12.\n\x0b\x61udio_range\x18\x0f \x01(\x0b\x32\x19.nuance.nlu.v1.AudioRange\x1aV\n\rEntitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.nuance.nlu.v1.SingleIntentEntityList:\x02\x38\x01\x42\r\n\x0bvalue_unionB:\n\x15\x63om.nuance.rpc.nlu.v1B\x1fSingleIntentInterpretationProtoP\x01\x62\x06proto3'
  ,
  dependencies=[nuance_dot_nlu_dot_v1_dot_interpretation__common__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_SINGLEINTENTINTERPRETATION_ENTITIESENTRY = _descriptor.Descriptor(
  name='EntitiesEntry',
  full_name='nuance.nlu.v1.SingleIntentInterpretation.EntitiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='nuance.nlu.v1.SingleIntentInterpretation.EntitiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='nuance.nlu.v1.SingleIntentInterpretation.EntitiesEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=411,
)

_SINGLEINTENTINTERPRETATION = _descriptor.Descriptor(
  name='SingleIntentInterpretation',
  full_name='nuance.nlu.v1.SingleIntentInterpretation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='intent', full_name='nuance.nlu.v1.SingleIntentInterpretation.intent', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='nuance.nlu.v1.SingleIntentInterpretation.confidence', index=1,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin', full_name='nuance.nlu.v1.SingleIntentInterpretation.origin', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entities', full_name='nuance.nlu.v1.SingleIntentInterpretation.entities', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SINGLEINTENTINTERPRETATION_ENTITIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=411,
)


_SINGLEINTENTENTITYLIST = _descriptor.Descriptor(
  name='SingleIntentEntityList',
  full_name='nuance.nlu.v1.SingleIntentEntityList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entities', full_name='nuance.nlu.v1.SingleIntentEntityList.entities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=413,
  serialized_end=490,
)


_SINGLEINTENTENTITY_ENTITIESENTRY = _descriptor.Descriptor(
  name='EntitiesEntry',
  full_name='nuance.nlu.v1.SingleIntentEntity.EntitiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='nuance.nlu.v1.SingleIntentEntity.EntitiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='nuance.nlu.v1.SingleIntentEntity.EntitiesEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=411,
)

_SINGLEINTENTENTITY = _descriptor.Descriptor(
  name='SingleIntentEntity',
  full_name='nuance.nlu.v1.SingleIntentEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text_range', full_name='nuance.nlu.v1.SingleIntentEntity.text_range', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='nuance.nlu.v1.SingleIntentEntity.confidence', index=1,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin', full_name='nuance.nlu.v1.SingleIntentEntity.origin', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entities', full_name='nuance.nlu.v1.SingleIntentEntity.entities', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='nuance.nlu.v1.SingleIntentEntity.string_value', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='struct_value', full_name='nuance.nlu.v1.SingleIntentEntity.struct_value', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='literal', full_name='nuance.nlu.v1.SingleIntentEntity.literal', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio_range', full_name='nuance.nlu.v1.SingleIntentEntity.audio_range', index=7,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SINGLEINTENTENTITY_ENTITIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value_union', full_name='nuance.nlu.v1.SingleIntentEntity.value_union',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=493,
  serialized_end=930,
)

_SINGLEINTENTINTERPRETATION_ENTITIESENTRY.fields_by_name['value'].message_type = _SINGLEINTENTENTITYLIST
_SINGLEINTENTINTERPRETATION_ENTITIESENTRY.containing_type = _SINGLEINTENTINTERPRETATION
_SINGLEINTENTINTERPRETATION.fields_by_name['origin'].enum_type = nuance_dot_nlu_dot_v1_dot_interpretation__common__pb2._ENUMORIGIN
_SINGLEINTENTINTERPRETATION.fields_by_name['entities'].message_type = _SINGLEINTENTINTERPRETATION_ENTITIESENTRY
_SINGLEINTENTENTITYLIST.fields_by_name['entities'].message_type = _SINGLEINTENTENTITY
_SINGLEINTENTENTITY_ENTITIESENTRY.fields_by_name['value'].message_type = _SINGLEINTENTENTITYLIST
_SINGLEINTENTENTITY_ENTITIESENTRY.containing_type = _SINGLEINTENTENTITY
_SINGLEINTENTENTITY.fields_by_name['text_range'].message_type = nuance_dot_nlu_dot_v1_dot_interpretation__common__pb2._TEXTRANGE
_SINGLEINTENTENTITY.fields_by_name['origin'].enum_type = nuance_dot_nlu_dot_v1_dot_interpretation__common__pb2._ENUMORIGIN
_SINGLEINTENTENTITY.fields_by_name['entities'].message_type = _SINGLEINTENTENTITY_ENTITIESENTRY
_SINGLEINTENTENTITY.fields_by_name['struct_value'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SINGLEINTENTENTITY.fields_by_name['audio_range'].message_type = nuance_dot_nlu_dot_v1_dot_interpretation__common__pb2._AUDIORANGE
_SINGLEINTENTENTITY.oneofs_by_name['value_union'].fields.append(
  _SINGLEINTENTENTITY.fields_by_name['string_value'])
_SINGLEINTENTENTITY.fields_by_name['string_value'].containing_oneof = _SINGLEINTENTENTITY.oneofs_by_name['value_union']
_SINGLEINTENTENTITY.oneofs_by_name['value_union'].fields.append(
  _SINGLEINTENTENTITY.fields_by_name['struct_value'])
_SINGLEINTENTENTITY.fields_by_name['struct_value'].containing_oneof = _SINGLEINTENTENTITY.oneofs_by_name['value_union']
DESCRIPTOR.message_types_by_name['SingleIntentInterpretation'] = _SINGLEINTENTINTERPRETATION
DESCRIPTOR.message_types_by_name['SingleIntentEntityList'] = _SINGLEINTENTENTITYLIST
DESCRIPTOR.message_types_by_name['SingleIntentEntity'] = _SINGLEINTENTENTITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SingleIntentInterpretation = _reflection.GeneratedProtocolMessageType('SingleIntentInterpretation', (_message.Message,), {

  'EntitiesEntry' : _reflection.GeneratedProtocolMessageType('EntitiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _SINGLEINTENTINTERPRETATION_ENTITIESENTRY,
    '__module__' : 'nuance.nlu.v1.single_intent_interpretation_pb2'
    # @@protoc_insertion_point(class_scope:nuance.nlu.v1.SingleIntentInterpretation.EntitiesEntry)
    })
  ,
  'DESCRIPTOR' : _SINGLEINTENTINTERPRETATION,
  '__module__' : 'nuance.nlu.v1.single_intent_interpretation_pb2'
  # @@protoc_insertion_point(class_scope:nuance.nlu.v1.SingleIntentInterpretation)
  })
_sym_db.RegisterMessage(SingleIntentInterpretation)
_sym_db.RegisterMessage(SingleIntentInterpretation.EntitiesEntry)

SingleIntentEntityList = _reflection.GeneratedProtocolMessageType('SingleIntentEntityList', (_message.Message,), {
  'DESCRIPTOR' : _SINGLEINTENTENTITYLIST,
  '__module__' : 'nuance.nlu.v1.single_intent_interpretation_pb2'
  # @@protoc_insertion_point(class_scope:nuance.nlu.v1.SingleIntentEntityList)
  })
_sym_db.RegisterMessage(SingleIntentEntityList)

SingleIntentEntity = _reflection.GeneratedProtocolMessageType('SingleIntentEntity', (_message.Message,), {

  'EntitiesEntry' : _reflection.GeneratedProtocolMessageType('EntitiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _SINGLEINTENTENTITY_ENTITIESENTRY,
    '__module__' : 'nuance.nlu.v1.single_intent_interpretation_pb2'
    # @@protoc_insertion_point(class_scope:nuance.nlu.v1.SingleIntentEntity.EntitiesEntry)
    })
  ,
  'DESCRIPTOR' : _SINGLEINTENTENTITY,
  '__module__' : 'nuance.nlu.v1.single_intent_interpretation_pb2'
  # @@protoc_insertion_point(class_scope:nuance.nlu.v1.SingleIntentEntity)
  })
_sym_db.RegisterMessage(SingleIntentEntity)
_sym_db.RegisterMessage(SingleIntentEntity.EntitiesEntry)


DESCRIPTOR._options = None
_SINGLEINTENTINTERPRETATION_ENTITIESENTRY._options = None
_SINGLEINTENTENTITY_ENTITIESENTRY._options = None
# @@protoc_insertion_point(module_scope)
