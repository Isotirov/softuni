wagons = int(input())
train = [0] * wagons

command = input()

while not command == "End":
    current_command = command.split()
    to_do = current_command[0]
    if to_do == "add":
        people = int(current_command[1])
        train[-1] += people
    elif to_do == "insert":
        people = int(current_command[2])
        index = int(current_command[1])
        train[index] += people
    elif to_do == "leave":
        people = int(current_command[2])
        index = int(current_command[1])
        train[index] -= people
    command = input()
print(train)