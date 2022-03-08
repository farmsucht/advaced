# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blockchain.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x62lockchain.proto\x12\nblockchain\"\xe6\x01\n\x0c\x42lockRequest\x12\x12\n\x05index\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x19\n\x0cpreviousHash\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x16\n\ttimestamp\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x11\n\x04hash\x18\x07 \x01(\tH\x03\x88\x01\x01\x12\x16\n\tvalidator\x18\x08 \x01(\tH\x04\x88\x01\x01\x12\x16\n\tsignature\x18\t \x01(\tH\x05\x88\x01\x01\x42\x08\n\x06_indexB\x0f\n\r_previousHashB\x0c\n\n_timestampB\x07\n\x05_hashB\x0c\n\n_validatorB\x0c\n\n_signature\"\xfe\x01\n\x12TransactionRequest\x12\x13\n\x06sender\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\trecipient\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06\x61mount\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12\x11\n\x04type\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x16\n\ttimestamp\x18\x06 \x01(\tH\x04\x88\x01\x01\x12\x11\n\x04hash\x18\x07 \x01(\tH\x05\x88\x01\x01\x12\x16\n\tsignature\x18\x08 \x01(\tH\x06\x88\x01\x01\x42\t\n\x07_senderB\x0c\n\n_recipientB\t\n\x07_amountB\x07\n\x05_typeB\x0c\n\n_timestampB\x07\n\x05_hashB\x0c\n\n_signature\"\x8f\x01\n\x0bTransaction\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x11\n\trecipient\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\x12\x0b\n\x03\x66\x65\x65\x18\x04 \x01(\r\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\t\x12\x0c\n\x04hash\x18\x07 \x01(\t\x12\x11\n\tsignature\x18\x08 \x01(\t\"3\n\x0cTransactions\x12#\n\x02tx\x18\x01 \x03(\x0b\x32\x17.blockchain.Transaction\"\xba\x01\n\x05\x42lock\x12\r\n\x05index\x18\x01 \x01(\x03\x12\x14\n\x0cpreviousHash\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x0f\n\x07\x62\x61seFee\x18\x05 \x01(\r\x12#\n\x02tx\x18\x06 \x03(\x0b\x32\x17.blockchain.Transaction\x12\x0c\n\x04hash\x18\x07 \x01(\t\x12\x11\n\tvalidator\x18\x08 \x01(\t\x12\x11\n\tsignature\x18\t \x01(\t\"+\n\x06\x42locks\x12!\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x11.blockchain.Block2\x98\x02\n\nBlockchain\x12\x37\n\x08getBlock\x12\x18.blockchain.BlockRequest\x1a\x11.blockchain.Block\x12\x39\n\tgetBlocks\x12\x18.blockchain.BlockRequest\x1a\x12.blockchain.Blocks\x12I\n\x0egetTransaction\x12\x1e.blockchain.TransactionRequest\x1a\x17.blockchain.Transaction\x12K\n\x0fgetTransactions\x12\x1e.blockchain.TransactionRequest\x1a\x18.blockchain.Transactionsb\x06proto3')



_BLOCKREQUEST = DESCRIPTOR.message_types_by_name['BlockRequest']
_TRANSACTIONREQUEST = DESCRIPTOR.message_types_by_name['TransactionRequest']
_TRANSACTION = DESCRIPTOR.message_types_by_name['Transaction']
_TRANSACTIONS = DESCRIPTOR.message_types_by_name['Transactions']
_BLOCK = DESCRIPTOR.message_types_by_name['Block']
_BLOCKS = DESCRIPTOR.message_types_by_name['Blocks']
BlockRequest = _reflection.GeneratedProtocolMessageType('BlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKREQUEST,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:blockchain.BlockRequest)
  })
_sym_db.RegisterMessage(BlockRequest)

TransactionRequest = _reflection.GeneratedProtocolMessageType('TransactionRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONREQUEST,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:blockchain.TransactionRequest)
  })
_sym_db.RegisterMessage(TransactionRequest)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTION,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:blockchain.Transaction)
  })
_sym_db.RegisterMessage(Transaction)

Transactions = _reflection.GeneratedProtocolMessageType('Transactions', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONS,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:blockchain.Transactions)
  })
_sym_db.RegisterMessage(Transactions)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:blockchain.Block)
  })
_sym_db.RegisterMessage(Block)

Blocks = _reflection.GeneratedProtocolMessageType('Blocks', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKS,
  '__module__' : 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:blockchain.Blocks)
  })
_sym_db.RegisterMessage(Blocks)

_BLOCKCHAIN = DESCRIPTOR.services_by_name['Blockchain']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BLOCKREQUEST._serialized_start=33
  _BLOCKREQUEST._serialized_end=263
  _TRANSACTIONREQUEST._serialized_start=266
  _TRANSACTIONREQUEST._serialized_end=520
  _TRANSACTION._serialized_start=523
  _TRANSACTION._serialized_end=666
  _TRANSACTIONS._serialized_start=668
  _TRANSACTIONS._serialized_end=719
  _BLOCK._serialized_start=722
  _BLOCK._serialized_end=908
  _BLOCKS._serialized_start=910
  _BLOCKS._serialized_end=953
  _BLOCKCHAIN._serialized_start=956
  _BLOCKCHAIN._serialized_end=1236
# @@protoc_insertion_point(module_scope)
