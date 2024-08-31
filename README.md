# Test1

My First protocol buffers (protobuf) test

## Instructions

```sh
pip install protobuf

&"C:\protoc\bin\protoc.exe" --proto_path=./proto --pyi_out=./src ./proto/AddressBook.proto

python.exe .\src\__init__.py
```

## Notes

- **DO NOT** modify any file with *_pb2.py* suffix in the filename. These files are meant to be auto generated with protoc cli tool from source .proto files in proto folder.