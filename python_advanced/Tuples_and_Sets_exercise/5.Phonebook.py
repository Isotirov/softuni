info = input()

contacts = {}

while "-" in info:
    contact, phone = info.split("-")
    contacts[contact] = phone
    info = input()

n = int(info)

for _ in range(n):
    contact = input()
    if contact not in contacts:
        print(f"Contact {contact} does not exist.")
    else:
        print(f"{contact} -> {contacts[contact]}")