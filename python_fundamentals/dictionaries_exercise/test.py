numbers = [int(x) for x in input().split()]

command = input()

while not command == "Finish":
    current_command = command.split()
    action = current_command[0]
    if action == "Add":
        value = int(current_command[1])
        numbers.append(value)
    elif "Remove":
        value = int(current_command[1])
        if value in numbers:
            numbers.remove(value)