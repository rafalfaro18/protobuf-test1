import AddressBook_pb2
import google.protobuf.text_format as text_format
import os

file_name = os.path.join("./tests/", "AddressBook.textproto")

address_book = AddressBook_pb2.AddressBook()
person = address_book.people.add()

person.id = 2345
person.name = "John Doe 2"
person.email = "example@example.com"
phone = person.phones.add()
phone.number = "8888-8888"
phone.type = AddressBook_pb2.Person.PHONE_TYPE_MOBILE

person2 = address_book.people.add()

person2.id = 2345
person2.name = "John Doe 2"
person2.email = "example@example.com"
phone2 = person2.phones.add()
phone2.number = "8888-8888"
phone2.type = AddressBook_pb2.Person.PHONE_TYPE_MOBILE

ab_text = text_format.MessageToString(address_book)

# Save address book
with open(file_name, "wt") as f:
  f.write(ab_text)
  f.close()

address_book2 = AddressBook_pb2.AddressBook()

# Read the existing address book.
with open(file_name, "rt") as f:
  ab2_text = f.read()
  text_format.Parse(ab2_text, address_book2)
  f.close()

print(address_book2.people.pop().name)