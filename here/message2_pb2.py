# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message2.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessage2.proto\x12\x0e\x65ncryptmessage\"^\n\x06Person\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0f\n\x02id\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x14\n\x07message\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x07\n\x05_nameB\x05\n\x03_idB\n\n\x08_message\" \n\rdecodeRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"!\n\x0e\x64\x65\x63odeResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\" \n\rencodeRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"!\n\x0e\x65ncodeResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xad\x01\n\x07\x44\x65\x63oder\x12P\n\rdecodeMessage\x12\x1d.encryptmessage.decodeRequest\x1a\x1e.encryptmessage.decodeResponse\"\x00\x12P\n\rencodeMessage\x12\x1d.encryptmessage.encodeRequest\x1a\x1e.encryptmessage.encodeResponse\"\x00\x62\x06proto3')



_PERSON = DESCRIPTOR.message_types_by_name['Person']
_DECODEREQUEST = DESCRIPTOR.message_types_by_name['decodeRequest']
_DECODERESPONSE = DESCRIPTOR.message_types_by_name['decodeResponse']
_ENCODEREQUEST = DESCRIPTOR.message_types_by_name['encodeRequest']
_ENCODERESPONSE = DESCRIPTOR.message_types_by_name['encodeResponse']
Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'message2_pb2'
  # @@protoc_insertion_point(class_scope:encryptmessage.Person)
  })
_sym_db.RegisterMessage(Person)

decodeRequest = _reflection.GeneratedProtocolMessageType('decodeRequest', (_message.Message,), {
  'DESCRIPTOR' : _DECODEREQUEST,
  '__module__' : 'message2_pb2'
  # @@protoc_insertion_point(class_scope:encryptmessage.decodeRequest)
  })
_sym_db.RegisterMessage(decodeRequest)

decodeResponse = _reflection.GeneratedProtocolMessageType('decodeResponse', (_message.Message,), {
  'DESCRIPTOR' : _DECODERESPONSE,
  '__module__' : 'message2_pb2'
  # @@protoc_insertion_point(class_scope:encryptmessage.decodeResponse)
  })
_sym_db.RegisterMessage(decodeResponse)

encodeRequest = _reflection.GeneratedProtocolMessageType('encodeRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENCODEREQUEST,
  '__module__' : 'message2_pb2'
  # @@protoc_insertion_point(class_scope:encryptmessage.encodeRequest)
  })
_sym_db.RegisterMessage(encodeRequest)

encodeResponse = _reflection.GeneratedProtocolMessageType('encodeResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENCODERESPONSE,
  '__module__' : 'message2_pb2'
  # @@protoc_insertion_point(class_scope:encryptmessage.encodeResponse)
  })
_sym_db.RegisterMessage(encodeResponse)

_DECODER = DESCRIPTOR.services_by_name['Decoder']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PERSON._serialized_start=34
  _PERSON._serialized_end=128
  _DECODEREQUEST._serialized_start=130
  _DECODEREQUEST._serialized_end=162
  _DECODERESPONSE._serialized_start=164
  _DECODERESPONSE._serialized_end=197
  _ENCODEREQUEST._serialized_start=199
  _ENCODEREQUEST._serialized_end=231
  _ENCODERESPONSE._serialized_start=233
  _ENCODERESPONSE._serialized_end=266
  _DECODER._serialized_start=269
  _DECODER._serialized_end=442
# @@protoc_insertion_point(module_scope)
