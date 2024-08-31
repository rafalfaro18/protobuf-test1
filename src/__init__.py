import AddressBook_pb2
import google.protobuf.text_format as text_format
import os

file_name_str = os.path.join("./tests/", "AddressBook.textproto")

address_book = AddressBook_pb2.AddressBook()
person = address_book.people.add()

person.id = 2345
person.name = "John Doe 2"
person.email = "example@example.com"
person.profile_picture = bytes("Test String", "utf-8")
phone = person.phones.add()
phone.number = "8888-8888"
phone.type = AddressBook_pb2.Person.PHONE_TYPE_MOBILE

person2 = address_book.people.add()

person2.id = 2345
person2.name = "John Doe 3"
person2.email = "example3@example.com"
phone2 = person2.phones.add()
phone2.number = "8888-8889"
phone2.type = AddressBook_pb2.Person.PHONE_TYPE_MOBILE

ab_text = text_format.MessageToString(address_book)

# Save address book as text format
with open(file_name_str, "wt") as f:
  f.write(ab_text)
  f.close()

address_book2 = AddressBook_pb2.AddressBook()

# Read the existing address book from text format.
with open(file_name_str, "rt") as f:
  ab2_text = f.read()
  text_format.Parse(ab2_text, address_book2)
  f.close()

print(address_book2.people.__getitem__(0).name)
print(address_book2.people.__getitem__(1).name)
print(address_book2.people.__getitem__(0).profile_picture.decode("utf-8"))

file_name_bin = os.path.join("./tests/", "AddressBook.binpb")

# Save address book as binary 'Wire' format
with open(file_name_bin, "wb") as f:
  f.write(address_book.SerializeToString())
  f.close()

address_book3 = AddressBook_pb2.AddressBook()

# Read the existing address book from binary 'Wire' format.
with open(file_name_bin, "rb") as f:
  address_book3.ParseFromString(f.read())
  f.close()

print(address_book3.people.__getitem__(0).name)
print(address_book3.people.__getitem__(1).name)
print(address_book3.people.__getitem__(0).profile_picture.decode("utf-8"))