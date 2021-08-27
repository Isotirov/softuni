item_journal = [x for x in input().split(", ")]

command = input()

while not command == "Craft!":
    current_command = command.split(" - ")
    to_do = current_command[0]
    if to_do == "Collect":
        item = current_command[1]
        if item not in item_journal:
            item_journal.append(item)
    elif to_do == "Drop":
        item = current_command[1]
        if item in item_journal:
            item_journal.remove(item)
    elif to_do == "Combine Items":
        old_item = current_command[1].split(":")[0]
        new_item = current_command[1].split(":")[1]
        if old_item in item_journal:
            old_item_index = item_journal.index(old_item)
            item_journal.insert(old_item_index+1, new_item)
    elif to_do == "Renew":
        item = current_command[1]
        if item in item_journal:
            item_journal.append(item)
            item_journal.remove(item)
    command = input()
print(", ".join(item_journal))