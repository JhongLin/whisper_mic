# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: faster_whisper_transcription.proto
# Protobuf Python Version: 4.25.1
# pylint: skip-file
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()



DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"faster_whisper_transcription.proto\x12\x1c\x66\x61ster_whisper_transcription\"4\n\tAudioData\x12\x15\n\rndarray_bytes\x18\x01 \x01(\x0c\x12\x10\n\x08language\x18\x02 \x01(\t\"#\n\rTranscription\x12\x12\n\nprediction\x18\x01 \x01(\t2\x86\x01\n\x1a\x46\x61sterWhisperTranscription\x12h\n\nStreamData\x12\'.faster_whisper_transcription.AudioData\x1a+.faster_whisper_transcription.Transcription\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'faster_whisper_transcription_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_AUDIODATA']._serialized_start=68
  _globals['_AUDIODATA']._serialized_end=120
  _globals['_TRANSCRIPTION']._serialized_start=122
  _globals['_TRANSCRIPTION']._serialized_end=157
  _globals['_FASTERWHISPERTRANSCRIPTION']._serialized_start=160
  _globals['_FASTERWHISPERTRANSCRIPTION']._serialized_end=294
# @@protoc_insertion_point(module_scope)
