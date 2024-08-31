import AddressBook_pb2

file_name = "AddressBook.dump"
address_book = AddressBook_pb2.AddressBook()
person = address_book.people.add()

person.id = 2345
person.name = "John Doe 2"
person.email = "example@example.com"
phone = person.phones.add()
phone.number = "8888-8888"
phone.type = AddressBook_pb2.Person.PHONE_TYPE_MOBILE

# Save address book
with open(file_name, "wb") as f:
  f.write(address_book.SerializeToString())
  f.close()

address_book2 = AddressBook_pb2.AddressBook()

# Read the existing address book.
with open(file_name, "rb") as f:
  address_book2.ParseFromString(f.read())
  f.close()

print(address_book2.people.pop().name)