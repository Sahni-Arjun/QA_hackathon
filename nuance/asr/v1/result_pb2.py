# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nuance/asr/v1/result.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nuance/asr/v1/result.proto',
  package='nuance.asr.v1',
  syntax='proto3',
  serialized_options=b'B\017NuanceAsrResult',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1anuance/asr/v1/result.proto\x12\rnuance.asr.v1\"\xcb\x01\n\x06Result\x12\x32\n\x0bresult_type\x18\x01 \x01(\x0e\x32\x1d.nuance.asr.v1.EnumResultType\x12\x14\n\x0c\x61\x62s_start_ms\x18\x02 \x01(\r\x12\x12\n\nabs_end_ms\x18\x03 \x01(\r\x12\x34\n\x0eutterance_info\x18\x04 \x01(\x0b\x32\x1c.nuance.asr.v1.UtteranceInfo\x12-\n\nhypotheses\x18\x05 \x03(\x0b\x32\x19.nuance.asr.v1.Hypothesis\"\xa6\x01\n\rUtteranceInfo\x12\x13\n\x0b\x64uration_ms\x18\x01 \x01(\r\x12\x1c\n\x14\x63lipping_duration_ms\x18\x02 \x01(\r\x12\x1e\n\x16\x64ropped_speech_packets\x18\x03 \x01(\r\x12!\n\x19\x64ropped_nonspeech_packets\x18\x04 \x01(\r\x12\x1f\n\x03\x64sp\x18\x05 \x01(\x0b\x32\x12.nuance.asr.v1.Dsp\"\xa2\x01\n\x03\x44sp\x12\x17\n\x0fsnr_estimate_db\x18\x01 \x01(\x02\x12\r\n\x05level\x18\x02 \x01(\x02\x12\x14\n\x0cnum_channels\x18\x03 \x01(\r\x12\x1a\n\x12initial_silence_ms\x18\x04 \x01(\r\x12\x16\n\x0einitial_energy\x18\x05 \x01(\x02\x12\x14\n\x0c\x66inal_energy\x18\x06 \x01(\x02\x12\x13\n\x0bmean_energy\x18\x07 \x01(\x02\"\xd4\x02\n\nHypothesis\x12\x14\n\nconfidence\x18\x01 \x01(\x02H\x00\x12\x1c\n\x12\x61verage_confidence\x18\x02 \x01(\x02H\x01\x12\x10\n\x08rejected\x18\x03 \x01(\x08\x12\x16\n\x0e\x66ormatted_text\x18\x04 \x01(\t\x12 \n\x18minimally_formatted_text\x18\x05 \x01(\t\x12\"\n\x05words\x18\x06 \x03(\x0b\x32\x13.nuance.asr.v1.Word\x12\x1e\n\x16\x65ncrypted_tokenization\x18\x07 \x01(\t\x12\x14\n\ngrammar_id\x18\t \x01(\tH\x02\x42 \n\x1eoptional_hypothesis_confidenceB(\n&optional_hypothesis_average_confidenceB \n\x1eoptional_hypothesis_grammar_id\"\xbd\x01\n\x04Word\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x14\n\nconfidence\x18\x02 \x01(\x02H\x00\x12\x10\n\x08start_ms\x18\x03 \x01(\r\x12\x0e\n\x06\x65nd_ms\x18\x04 \x01(\r\x12\x1d\n\x15silence_after_word_ms\x18\x05 \x01(\r\x12\x16\n\x0cgrammar_rule\x18\x06 \x01(\tH\x01\x42\x1a\n\x18optional_word_confidenceB\x1c\n\x1aoptional_word_grammar_rule*?\n\x0e\x45numResultType\x12\t\n\x05\x46INAL\x10\x00\x12\x0b\n\x07PARTIAL\x10\x01\x12\x15\n\x11IMMUTABLE_PARTIAL\x10\x02\x42\x11\x42\x0fNuanceAsrResultb\x06proto3'
)

_ENUMRESULTTYPE = _descriptor.EnumDescriptor(
  name='EnumResultType',
  full_name='nuance.asr.v1.EnumResultType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FINAL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PARTIAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IMMUTABLE_PARTIAL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1120,
  serialized_end=1183,
)
_sym_db.RegisterEnumDescriptor(_ENUMRESULTTYPE)

EnumResultType = enum_type_wrapper.EnumTypeWrapper(_ENUMRESULTTYPE)
FINAL = 0
PARTIAL = 1
IMMUTABLE_PARTIAL = 2



_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='nuance.asr.v1.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_type', full_name='nuance.asr.v1.Result.result_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='abs_start_ms', full_name='nuance.asr.v1.Result.abs_start_ms', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='abs_end_ms', full_name='nuance.asr.v1.Result.abs_end_ms', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='utterance_info', full_name='nuance.asr.v1.Result.utterance_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hypotheses', full_name='nuance.asr.v1.Result.hypotheses', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=46,
  serialized_end=249,
)


_UTTERANCEINFO = _descriptor.Descriptor(
  name='UtteranceInfo',
  full_name='nuance.asr.v1.UtteranceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='duration_ms', full_name='nuance.asr.v1.UtteranceInfo.duration_ms', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clipping_duration_ms', full_name='nuance.asr.v1.UtteranceInfo.clipping_duration_ms', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dropped_speech_packets', full_name='nuance.asr.v1.UtteranceInfo.dropped_speech_packets', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dropped_nonspeech_packets', full_name='nuance.asr.v1.UtteranceInfo.dropped_nonspeech_packets', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dsp', full_name='nuance.asr.v1.UtteranceInfo.dsp', index=4,
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
  serialized_start=252,
  serialized_end=418,
)


_DSP = _descriptor.Descriptor(
  name='Dsp',
  full_name='nuance.asr.v1.Dsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='snr_estimate_db', full_name='nuance.asr.v1.Dsp.snr_estimate_db', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='nuance.asr.v1.Dsp.level', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_channels', full_name='nuance.asr.v1.Dsp.num_channels', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='initial_silence_ms', full_name='nuance.asr.v1.Dsp.initial_silence_ms', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='initial_energy', full_name='nuance.asr.v1.Dsp.initial_energy', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='final_energy', full_name='nuance.asr.v1.Dsp.final_energy', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mean_energy', full_name='nuance.asr.v1.Dsp.mean_energy', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_end=583,
)


_HYPOTHESIS = _descriptor.Descriptor(
  name='Hypothesis',
  full_name='nuance.asr.v1.Hypothesis',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='confidence', full_name='nuance.asr.v1.Hypothesis.confidence', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='average_confidence', full_name='nuance.asr.v1.Hypothesis.average_confidence', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rejected', full_name='nuance.asr.v1.Hypothesis.rejected', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='formatted_text', full_name='nuance.asr.v1.Hypothesis.formatted_text', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minimally_formatted_text', full_name='nuance.asr.v1.Hypothesis.minimally_formatted_text', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='words', full_name='nuance.asr.v1.Hypothesis.words', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='encrypted_tokenization', full_name='nuance.asr.v1.Hypothesis.encrypted_tokenization', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grammar_id', full_name='nuance.asr.v1.Hypothesis.grammar_id', index=7,
      number=9, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='optional_hypothesis_confidence', full_name='nuance.asr.v1.Hypothesis.optional_hypothesis_confidence',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_hypothesis_average_confidence', full_name='nuance.asr.v1.Hypothesis.optional_hypothesis_average_confidence',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_hypothesis_grammar_id', full_name='nuance.asr.v1.Hypothesis.optional_hypothesis_grammar_id',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=586,
  serialized_end=926,
)


_WORD = _descriptor.Descriptor(
  name='Word',
  full_name='nuance.asr.v1.Word',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='nuance.asr.v1.Word.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='nuance.asr.v1.Word.confidence', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_ms', full_name='nuance.asr.v1.Word.start_ms', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_ms', full_name='nuance.asr.v1.Word.end_ms', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='silence_after_word_ms', full_name='nuance.asr.v1.Word.silence_after_word_ms', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grammar_rule', full_name='nuance.asr.v1.Word.grammar_rule', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='optional_word_confidence', full_name='nuance.asr.v1.Word.optional_word_confidence',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_word_grammar_rule', full_name='nuance.asr.v1.Word.optional_word_grammar_rule',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=929,
  serialized_end=1118,
)

_RESULT.fields_by_name['result_type'].enum_type = _ENUMRESULTTYPE
_RESULT.fields_by_name['utterance_info'].message_type = _UTTERANCEINFO
_RESULT.fields_by_name['hypotheses'].message_type = _HYPOTHESIS
_UTTERANCEINFO.fields_by_name['dsp'].message_type = _DSP
_HYPOTHESIS.fields_by_name['words'].message_type = _WORD
_HYPOTHESIS.oneofs_by_name['optional_hypothesis_confidence'].fields.append(
  _HYPOTHESIS.fields_by_name['confidence'])
_HYPOTHESIS.fields_by_name['confidence'].containing_oneof = _HYPOTHESIS.oneofs_by_name['optional_hypothesis_confidence']
_HYPOTHESIS.oneofs_by_name['optional_hypothesis_average_confidence'].fields.append(
  _HYPOTHESIS.fields_by_name['average_confidence'])
_HYPOTHESIS.fields_by_name['average_confidence'].containing_oneof = _HYPOTHESIS.oneofs_by_name['optional_hypothesis_average_confidence']
_HYPOTHESIS.oneofs_by_name['optional_hypothesis_grammar_id'].fields.append(
  _HYPOTHESIS.fields_by_name['grammar_id'])
_HYPOTHESIS.fields_by_name['grammar_id'].containing_oneof = _HYPOTHESIS.oneofs_by_name['optional_hypothesis_grammar_id']
_WORD.oneofs_by_name['optional_word_confidence'].fields.append(
  _WORD.fields_by_name['confidence'])
_WORD.fields_by_name['confidence'].containing_oneof = _WORD.oneofs_by_name['optional_word_confidence']
_WORD.oneofs_by_name['optional_word_grammar_rule'].fields.append(
  _WORD.fields_by_name['grammar_rule'])
_WORD.fields_by_name['grammar_rule'].containing_oneof = _WORD.oneofs_by_name['optional_word_grammar_rule']
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['UtteranceInfo'] = _UTTERANCEINFO
DESCRIPTOR.message_types_by_name['Dsp'] = _DSP
DESCRIPTOR.message_types_by_name['Hypothesis'] = _HYPOTHESIS
DESCRIPTOR.message_types_by_name['Word'] = _WORD
DESCRIPTOR.enum_types_by_name['EnumResultType'] = _ENUMRESULTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'nuance.asr.v1.result_pb2'
  # @@protoc_insertion_point(class_scope:nuance.asr.v1.Result)
  })
_sym_db.RegisterMessage(Result)

UtteranceInfo = _reflection.GeneratedProtocolMessageType('UtteranceInfo', (_message.Message,), {
  'DESCRIPTOR' : _UTTERANCEINFO,
  '__module__' : 'nuance.asr.v1.result_pb2'
  # @@protoc_insertion_point(class_scope:nuance.asr.v1.UtteranceInfo)
  })
_sym_db.RegisterMessage(UtteranceInfo)

Dsp = _reflection.GeneratedProtocolMessageType('Dsp', (_message.Message,), {
  'DESCRIPTOR' : _DSP,
  '__module__' : 'nuance.asr.v1.result_pb2'
  # @@protoc_insertion_point(class_scope:nuance.asr.v1.Dsp)
  })
_sym_db.RegisterMessage(Dsp)

Hypothesis = _reflection.GeneratedProtocolMessageType('Hypothesis', (_message.Message,), {
  'DESCRIPTOR' : _HYPOTHESIS,
  '__module__' : 'nuance.asr.v1.result_pb2'
  # @@protoc_insertion_point(class_scope:nuance.asr.v1.Hypothesis)
  })
_sym_db.RegisterMessage(Hypothesis)

Word = _reflection.GeneratedProtocolMessageType('Word', (_message.Message,), {
  'DESCRIPTOR' : _WORD,
  '__module__' : 'nuance.asr.v1.result_pb2'
  # @@protoc_insertion_point(class_scope:nuance.asr.v1.Word)
  })
_sym_db.RegisterMessage(Word)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
