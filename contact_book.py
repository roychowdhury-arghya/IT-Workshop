contacts = {}

# load contacts
try:
    with open("contacts.txt", "r") as f:
        for line in f:
            name, phone, email = line.strip().split(",")
            contacts[name] = (phone, email)
except FileNotFoundError:
    pass

# add contact
name = input("Enter name: ")
phone = input("Enter phone: ")
email = input("Enter email: ")
contacts[name] = (phone, email)

# search contact
search = input("Search name: ")
if search in contacts:
    print(contacts[search])
else:
    print("Not found")

# list contacts
print("\nAll Contacts:")
for name, info in contacts.items():
    print(name, info)

# save contacts
with open("contacts.txt", "w") as f:
    for name, info in contacts.items():
        f.write(f"{name},{info[0]},{info[1]}\n")
