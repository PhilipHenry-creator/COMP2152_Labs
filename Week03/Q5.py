contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-999"
}
print(f"Alice's number: {contacts['Alice']}")
contacts["Diana"] = "555-4321"
print(f"Contacts after adding Diana: {contacts}")
contacts["Bob"] = "555-0000"
print(f"Contacts after adding Bob: {contacts}")
del contacts["Charlie"]
print(f"Contacts after adding Charlie: {contacts}")
print(f"All Names: {contacts.keys()}")
print(f"All Numbers: {contacts.values()}")
print(f"Total contacts: {len(contacts)}")