to_do_list = [0] * 10

command = input()

while not command == "End":
    current_command = command.split("-")
    importance = int(current_command[0])
    note = current_command[1]
    to_do_list.insert(importance, note)
    command = input()
print([x for x in to_do_list if not x == 0])