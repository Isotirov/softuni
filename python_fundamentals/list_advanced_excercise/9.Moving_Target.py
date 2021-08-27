targets = [int(x) for x in input().split()]

command = input()

while not command == "End":
    current_command = command.split()
    to_do = current_command[0]
    index = int(current_command[1])
    if to_do == "Shoot":
        power = int(current_command[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif to_do == "Add":
        value = int(current_command[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif to_do == "Strike":
        radius = int(current_command[2])
        if index - radius >= 0 and index + radius < len(targets):
            for i in range(index+radius, index - radius-1, -1):
                targets.pop(i)
        else:
            print("Strike missed!")
    command = input()
print(*targets, sep="|")