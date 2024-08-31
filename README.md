# Protobuf Test1

My First protocol buffers (protobuf) test

## Instructions

```sh
pip install protobuf

&"C:\protoc\bin\protoc.exe" --proto_path=./proto --python_out=./src ./proto/AddressBook.proto
&"C:\protoc\bin\protoc.exe" --proto_path=./proto --pyi_out=./src ./proto/AddressBook.proto
&"C:\protoc\bin\protoc.exe" --proto_path=./proto --plugin="protoc-gen-js=C:\protobuf-javascript\bin\protoc-gen-js.exe" --js_out=./src ./proto/AddressBook.proto

python.exe .\src\__init__.py
```

## Notes

- **.textproto** is a legacy file extension that was recently replaced by **.txtpb** as described in [Buf's Image Formats documentation](https://buf.build/docs/reference/inputs#image-formats). I'm using .textproto just because I'm learning how those files are being used in another project I'm interested in [(libiamf)](https://github.com/AOMediaCodec/libiamf) see [tests folder](https://github.com/AOMediaCodec/libiamf/tree/main/tests) for sample .textproto files.

- To use --js_out download an extract [this plugin](https://github.com/protocolbuffers/protobuf-javascript/releases).

- **DO NOT** modify any file with *_pb2.py* or *_pb2.pyi* suffix in the filename. These files are meant to be auto generated with protoc cli tool from source .proto files in proto folder.