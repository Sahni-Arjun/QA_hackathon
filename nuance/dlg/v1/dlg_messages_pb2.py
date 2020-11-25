# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nuance/dlg/v1/dlg_messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nuance.asr.v1 import recognizer_pb2 as nuance_dot_asr_dot_v1_dot_recognizer__pb2
from nuance.asr.v1 import result_pb2 as nuance_dot_asr_dot_v1_dot_result__pb2
from nuance.tts.v1 import nuance_tts_pb2 as nuance_dot_tts_dot_v1_dot_nuance__tts__pb2
from nuance.dlg.v1.common import dlg_common_messages_pb2 as nuance_dot_dlg_dot_v1_dot_common_dot_dlg__common__messages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nuance/dlg/v1/dlg_messages.proto',
  package='nuance.dlg.v1',
  syntax='proto3',
  serialized_options=b'\n.com.nuance.coretech.dialog.v1.service.messagesP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n nuance/dlg/v1/dlg_messages.proto\x12\rnuance.dlg.v1\x1a\x1enuance/asr/v1/recognizer.proto\x1a\x1anuance/asr/v1/result.proto\x1a\x1enuance/tts/v1/nuance_tts.proto\x1a.nuance/dlg/v1/common/dlg_common_messages.proto\"\xe2\x01\n\x0bStreamInput\x12.\n\x07request\x18\x01 \x01(\x0b\x32\x1d.nuance.dlg.v1.ExecuteRequest\x12\x34\n\x0e\x61sr_control_v1\x18\x02 \x01(\x0b\x32\x1a.nuance.dlg.v1.AsrParamsV1H\x00\x12\r\n\x05\x61udio\x18\x03 \x01(\x0c\x12\x34\n\x0etts_control_v1\x18\x04 \x01(\x0b\x32\x1a.nuance.dlg.v1.TtsParamsV1H\x01\x42\x13\n\x11\x61sr_control_oneofB\x13\n\x11tts_control_oneof\"\x82\x02\n\x0cStreamOutput\x12\x30\n\x08response\x18\x01 \x01(\x0b\x32\x1e.nuance.dlg.v1.ExecuteResponse\x12/\n\x05\x61udio\x18\x02 \x01(\x0b\x32 .nuance.tts.v1.SynthesisResponse\x12)\n\nasr_result\x18\x03 \x01(\x0b\x32\x15.nuance.asr.v1.Result\x12)\n\nasr_status\x18\x04 \x01(\x0b\x32\x15.nuance.asr.v1.Status\x12\x39\n\x13\x61sr_start_of_speech\x18\x05 \x01(\x0b\x32\x1c.nuance.asr.v1.StartOfSpeech\"\xb3\x02\n\x0cStartRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x30\n\x08selector\x18\x02 \x01(\x0b\x32\x1e.nuance.dlg.v1.common.Selector\x12:\n\x07payload\x18\x03 \x01(\x0b\x32).nuance.dlg.v1.common.StartRequestPayload\x12\x1b\n\x13session_timeout_sec\x18\x04 \x01(\r\x12\x0f\n\x07user_id\x18\x05 \x01(\t\x12@\n\x0b\x63lient_data\x18\x06 \x03(\x0b\x32+.nuance.dlg.v1.StartRequest.ClientDataEntry\x1a\x31\n\x0f\x43lientDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"L\n\rStartResponse\x12;\n\x07payload\x18\x01 \x01(\x0b\x32*.nuance.dlg.v1.common.StartResponsePayload\"\xa5\x01\n\x0e\x45xecuteRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x30\n\x08selector\x18\x02 \x01(\x0b\x32\x1e.nuance.dlg.v1.common.Selector\x12<\n\x07payload\x18\x03 \x01(\x0b\x32+.nuance.dlg.v1.common.ExecuteRequestPayload\x12\x0f\n\x07user_id\x18\x05 \x01(\t\"\xec\x03\n\x0b\x41srParamsV1\x12\x30\n\x0c\x61udio_format\x18\x01 \x01(\x0b\x32\x1a.nuance.asr.v1.AudioFormat\x12K\n\x18utterance_detection_mode\x18\x02 \x01(\x0e\x32).nuance.asr.v1.EnumUtteranceDetectionMode\x12:\n\x11recognition_flags\x18\x03 \x01(\x0b\x32\x1f.nuance.asr.v1.RecognitionFlags\x12\x32\n\x0bresult_type\x18\x04 \x01(\x0e\x32\x1d.nuance.asr.v1.EnumResultType\x12\x1b\n\x13no_input_timeout_ms\x18\x05 \x01(\r\x12\x1e\n\x16recognition_timeout_ms\x18\x06 \x01(\r\x12 \n\x18utterance_end_silence_ms\x18\x07 \x01(\r\x12&\n\x1cspeech_detection_sensitivity\x18\x08 \x01(\x02H\x00\x12\x16\n\x0emax_hypotheses\x18\t \x01(\r\x12&\n\x1e\x65nd_stream_no_valid_hypotheses\x18\n \x01(\x08\x42\'\n%optional_speech_detection_sensitivity\"h\n\x0bTtsParamsV1\x12\x34\n\x0c\x61udio_params\x18\x01 \x01(\x0b\x32\x1e.nuance.tts.v1.AudioParameters\x12#\n\x05voice\x18\x02 \x01(\x0b\x32\x14.nuance.tts.v1.Voice\"P\n\x0f\x45xecuteResponse\x12=\n\x07payload\x18\x01 \x01(\x0b\x32,.nuance.dlg.v1.common.ExecuteResponsePayload\"2\n\x0bStopRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x05 \x01(\t\"\x0e\n\x0cStopResponseB2\n.com.nuance.coretech.dialog.v1.service.messagesP\x01\x62\x06proto3'
  ,
  dependencies=[nuance_dot_asr_dot_v1_dot_recognizer__pb2.DESCRIPTOR,nuance_dot_asr_dot_v1_dot_result__pb2.DESCRIPTOR,nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.DESCRIPTOR,nuance_dot_dlg_dot_v1_dot_common_dot_dlg__common__messages__pb2.DESCRIPTOR,])




_STREAMINPUT = _descriptor.Descriptor(
  name='StreamInput',
  full_name='nuance.dlg.v1.StreamInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='nuance.dlg.v1.StreamInput.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asr_control_v1', full_name='nuance.dlg.v1.StreamInput.asr_control_v1', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio', full_name='nuance.dlg.v1.StreamInput.audio', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tts_control_v1', full_name='nuance.dlg.v1.StreamInput.tts_control_v1', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='asr_control_oneof', full_name='nuance.dlg.v1.StreamInput.asr_control_oneof',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='tts_control_oneof', full_name='nuance.dlg.v1.StreamInput.tts_control_oneof',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=192,
  serialized_end=418,
)


_STREAMOUTPUT = _descriptor.Descriptor(
  name='StreamOutput',
  full_name='nuance.dlg.v1.StreamOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='nuance.dlg.v1.StreamOutput.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio', full_name='nuance.dlg.v1.StreamOutput.audio', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asr_result', full_name='nuance.dlg.v1.StreamOutput.asr_result', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asr_status', full_name='nuance.dlg.v1.StreamOutput.asr_status', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asr_start_of_speech', full_name='nuance.dlg.v1.StreamOutput.asr_start_of_speech', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=421,
  serialized_end=679,
)


_STARTREQUEST_CLIENTDATAENTRY = _descriptor.Descriptor(
  name='ClientDataEntry',
  full_name='nuance.dlg.v1.StartRequest.ClientDataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='nuance.dlg.v1.StartRequest.ClientDataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='nuance.dlg.v1.StartRequest.ClientDataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=940,
  serialized_end=989,
)

_STARTREQUEST = _descriptor.Descriptor(
  name='StartRequest',
  full_name='nuance.dlg.v1.StartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='nuance.dlg.v1.StartRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='selector', full_name='nuance.dlg.v1.StartRequest.selector', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='nuance.dlg.v1.StartRequest.payload', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_timeout_sec', full_name='nuance.dlg.v1.StartRequest.session_timeout_sec', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='nuance.dlg.v1.StartRequest.user_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_data', full_name='nuance.dlg.v1.StartRequest.client_data', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_STARTREQUEST_CLIENTDATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=682,
  serialized_end=989,
)


_STARTRESPONSE = _descriptor.Descriptor(
  name='StartResponse',
  full_name='nuance.dlg.v1.StartResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='nuance.dlg.v1.StartResponse.payload', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=991,
  serialized_end=1067,
)


_EXECUTEREQUEST = _descriptor.Descriptor(
  name='ExecuteRequest',
  full_name='nuance.dlg.v1.ExecuteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='nuance.dlg.v1.ExecuteRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='selector', full_name='nuance.dlg.v1.ExecuteRequest.selector', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='nuance.dlg.v1.ExecuteRequest.payload', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='nuance.dlg.v1.ExecuteRequest.user_id', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1070,
  serialized_end=1235,
)


_ASRPARAMSV1 = _descriptor.Descriptor(
  name='AsrParamsV1',
  full_name='nuance.dlg.v1.AsrParamsV1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio_format', full_name='nuance.dlg.v1.AsrParamsV1.audio_format', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='utterance_detection_mode', full_name='nuance.dlg.v1.AsrParamsV1.utterance_detection_mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recognition_flags', full_name='nuance.dlg.v1.AsrParamsV1.recognition_flags', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_type', full_name='nuance.dlg.v1.AsrParamsV1.result_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='no_input_timeout_ms', full_name='nuance.dlg.v1.AsrParamsV1.no_input_timeout_ms', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recognition_timeout_ms', full_name='nuance.dlg.v1.AsrParamsV1.recognition_timeout_ms', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='utterance_end_silence_ms', full_name='nuance.dlg.v1.AsrParamsV1.utterance_end_silence_ms', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speech_detection_sensitivity', full_name='nuance.dlg.v1.AsrParamsV1.speech_detection_sensitivity', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_hypotheses', full_name='nuance.dlg.v1.AsrParamsV1.max_hypotheses', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_stream_no_valid_hypotheses', full_name='nuance.dlg.v1.AsrParamsV1.end_stream_no_valid_hypotheses', index=9,
      number=10, type=8, cpp_type=7, label=1,
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
    _descriptor.OneofDescriptor(
      name='optional_speech_detection_sensitivity', full_name='nuance.dlg.v1.AsrParamsV1.optional_speech_detection_sensitivity',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1238,
  serialized_end=1730,
)


_TTSPARAMSV1 = _descriptor.Descriptor(
  name='TtsParamsV1',
  full_name='nuance.dlg.v1.TtsParamsV1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio_params', full_name='nuance.dlg.v1.TtsParamsV1.audio_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voice', full_name='nuance.dlg.v1.TtsParamsV1.voice', index=1,
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
  serialized_start=1732,
  serialized_end=1836,
)


_EXECUTERESPONSE = _descriptor.Descriptor(
  name='ExecuteResponse',
  full_name='nuance.dlg.v1.ExecuteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='nuance.dlg.v1.ExecuteResponse.payload', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1838,
  serialized_end=1918,
)


_STOPREQUEST = _descriptor.Descriptor(
  name='StopRequest',
  full_name='nuance.dlg.v1.StopRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='nuance.dlg.v1.StopRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='nuance.dlg.v1.StopRequest.user_id', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1920,
  serialized_end=1970,
)


_STOPRESPONSE = _descriptor.Descriptor(
  name='StopResponse',
  full_name='nuance.dlg.v1.StopResponse',
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
  serialized_start=1972,
  serialized_end=1986,
)

_STREAMINPUT.fields_by_name['request'].message_type = _EXECUTEREQUEST
_STREAMINPUT.fields_by_name['asr_control_v1'].message_type = _ASRPARAMSV1
_STREAMINPUT.fields_by_name['tts_control_v1'].message_type = _TTSPARAMSV1
_STREAMINPUT.oneofs_by_name['asr_control_oneof'].fields.append(
  _STREAMINPUT.fields_by_name['asr_control_v1'])
_STREAMINPUT.fields_by_name['asr_control_v1'].containing_oneof = _STREAMINPUT.oneofs_by_name['asr_control_oneof']
_STREAMINPUT.oneofs_by_name['tts_control_oneof'].fields.append(
  _STREAMINPUT.fields_by_name['tts_control_v1'])
_STREAMINPUT.fields_by_name['tts_control_v1'].containing_oneof = _STREAMINPUT.oneofs_by_name['tts_control_oneof']
_STREAMOUTPUT.fields_by_name['response'].message_type = _EXECUTERESPONSE
_STREAMOUTPUT.fields_by_name['audio'].message_type = nuance_dot_tts_dot_v1_dot_nuance__tts__pb2._SYNTHESISRESPONSE
_STREAMOUTPUT.fields_by_name['asr_result'].message_type = nuance_dot_asr_dot_v1_dot_result__pb2._RESULT
_STREAMOUTPUT.fields_by_name['asr_status'].message_type = nuance_dot_asr_dot_v1_dot_recognizer__pb2._STATUS
_STREAMOUTPUT.fields_by_name['asr_start_of_speech'].message_type = nuance_dot_asr_dot_v1_dot_recognizer__pb2._STARTOFSPEECH
_STARTREQUEST_CLIENTDATAENTRY.containing_type = _STARTREQUEST
_STARTREQUEST.fields_by_name['selector'].message_type = nuance_dot_dlg_dot_v1_dot_common_dot_dlg__common__messages__pb2._SELECTOR
_STARTREQUEST.fields_by_name['payload'].message_type = nuance_dot_dlg_dot_v1_dot_common_dot_dlg__common__messages__pb2._STARTREQUESTPAYLOAD
_STARTREQUEST.fields_by_name['client_data'].message_type = _STARTREQUEST_CLIENTDATAENTRY
_STARTRESPONSE.fields_by_name['payload'].message_type = nuance_dot_dlg_dot_v1_dot_common_dot_dlg__common__messages__pb2._STARTRESPONSEPAYLOAD
_EXECUTEREQUEST.fields_by_name['selector'].message_type = nuance_dot_dlg_dot_v1_dot_common_dot_dlg__common__messages__pb2._SELECTOR
_EXECUTEREQUEST.fields_by_name['payload'].message_type = nuance_dot_dlg_dot_v1_dot_common_dot_dlg__common__messages__pb2._EXECUTEREQUESTPAYLOAD
_ASRPARAMSV1.fields_by_name['audio_format'].message_type = nuance_dot_asr_dot_v1_dot_recognizer__pb2._AUDIOFORMAT
_ASRPARAMSV1.fields_by_name['utterance_detection_mode'].enum_type = nuance_dot_asr_dot_v1_dot_recognizer__pb2._ENUMUTTERANCEDETECTIONMODE
_ASRPARAMSV1.fields_by_name['recognition_flags'].message_type = nuance_dot_asr_dot_v1_dot_recognizer__pb2._RECOGNITIONFLAGS
_ASRPARAMSV1.fields_by_name['result_type'].enum_type = nuance_dot_asr_dot_v1_dot_result__pb2._ENUMRESULTTYPE
_ASRPARAMSV1.oneofs_by_name['optional_speech_detection_sensitivity'].fields.append(
  _ASRPARAMSV1.fields_by_name['speech_detection_sensitivity'])
_ASRPARAMSV1.fields_by_name['speech_detection_sensitivity'].containing_oneof = _ASRPARAMSV1.oneofs_by_name['optional_speech_detection_sensitivity']
_TTSPARAMSV1.fields_by_name['audio_params'].message_type = nuance_dot_tts_dot_v1_dot_nuance__tts__pb2._AUDIOPARAMETERS
_TTSPARAMSV1.fields_by_name['voice'].message_type = nuance_dot_tts_dot_v1_dot_nuance__tts__pb2._VOICE
_EXECUTERESPONSE.fields_by_name['payload'].message_type = nuance_dot_dlg_dot_v1_dot_common_dot_dlg__common__messages__pb2._EXECUTERESPONSEPAYLOAD
DESCRIPTOR.message_types_by_name['StreamInput'] = _STREAMINPUT
DESCRIPTOR.message_types_by_name['StreamOutput'] = _STREAMOUTPUT
DESCRIPTOR.message_types_by_name['StartRequest'] = _STARTREQUEST
DESCRIPTOR.message_types_by_name['StartResponse'] = _STARTRESPONSE
DESCRIPTOR.message_types_by_name['ExecuteRequest'] = _EXECUTEREQUEST
DESCRIPTOR.message_types_by_name['AsrParamsV1'] = _ASRPARAMSV1
DESCRIPTOR.message_types_by_name['TtsParamsV1'] = _TTSPARAMSV1
DESCRIPTOR.message_types_by_name['ExecuteResponse'] = _EXECUTERESPONSE
DESCRIPTOR.message_types_by_name['StopRequest'] = _STOPREQUEST
DESCRIPTOR.message_types_by_name['StopResponse'] = _STOPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamInput = _reflection.GeneratedProtocolMessageType('StreamInput', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINPUT,
  '__module__' : 'nuance.dlg.v1.dlg_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dlg.v1.StreamInput)
  })
_sym_db.RegisterMessage(StreamInput)

StreamOutput = _reflection.GeneratedProtocolMessageType('StreamOutput', (_message.Message,), {
  'DESCRIPTOR' : _STREAMOUTPUT,
  '__module__' : 'nuance.dlg.v1.dlg_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dlg.v1.StreamOutput)
  })
_sym_db.RegisterMessage(StreamOutput)

StartRequest = _reflection.GeneratedProtocolMessageType('StartRequest', (_message.Message,), {

  'ClientDataEntry' : _reflection.GeneratedProtocolMessageType('ClientDataEntry', (_message.Message,), {
    'DESCRIPTOR' : _STARTREQUEST_CLIENTDATAENTRY,
    '__module__' : 'nuance.dlg.v1.dlg_messages_pb2'
    # @@protoc_insertion_point(class_scope:nuance.dlg.v1.StartRequest.ClientDataEntry)
    })
  ,
  'DESCRIPTOR' : _STARTREQUEST,
  '__module__' : 'nuance.dlg.v1.dlg_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dlg.v1.StartRequest)
  })
_sym_db.RegisterMessage(StartRequest)
_sym_db.RegisterMessage(StartRequest.ClientDataEntry)

StartResponse = _reflection.GeneratedProtocolMessageType('StartResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTRESPONSE,
  '__module__' : 'nuance.dlg.v1.dlg_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dlg.v1.StartResponse)
  })
_sym_db.RegisterMessage(StartResponse)

ExecuteRequest = _reflection.GeneratedProtocolMessageType('ExecuteRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEREQUEST,
  '__module__' : 'nuance.dlg.v1.dlg_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dlg.v1.ExecuteRequest)
  })
_sym_db.RegisterMessage(ExecuteRequest)

AsrParamsV1 = _reflection.GeneratedProtocolMessageType('AsrParamsV1', (_message.Message,), {
  'DESCRIPTOR' : _ASRPARAMSV1,
  '__module__' : 'nuance.dlg.v1.dlg_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dlg.v1.AsrParamsV1)
  })
_sym_db.RegisterMessage(AsrParamsV1)

TtsParamsV1 = _reflection.GeneratedProtocolMessageType('TtsParamsV1', (_message.Message,), {
  'DESCRIPTOR' : _TTSPARAMSV1,
  '__module__' : 'nuance.dlg.v1.dlg_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dlg.v1.TtsParamsV1)
  })
_sym_db.RegisterMessage(TtsParamsV1)

ExecuteResponse = _reflection.GeneratedProtocolMessageType('ExecuteResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTERESPONSE,
  '__module__' : 'nuance.dlg.v1.dlg_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dlg.v1.ExecuteResponse)
  })
_sym_db.RegisterMessage(ExecuteResponse)

StopRequest = _reflection.GeneratedProtocolMessageType('StopRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPREQUEST,
  '__module__' : 'nuance.dlg.v1.dlg_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dlg.v1.StopRequest)
  })
_sym_db.RegisterMessage(StopRequest)

StopResponse = _reflection.GeneratedProtocolMessageType('StopResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOPRESPONSE,
  '__module__' : 'nuance.dlg.v1.dlg_messages_pb2'
  # @@protoc_insertion_point(class_scope:nuance.dlg.v1.StopResponse)
  })
_sym_db.RegisterMessage(StopResponse)


DESCRIPTOR._options = None
_STARTREQUEST_CLIENTDATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
