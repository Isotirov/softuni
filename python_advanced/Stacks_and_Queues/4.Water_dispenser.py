from collections import deque

water_qt = int(input())
name = input()
people = deque()

while not name == "Start":
    people.append(name)
    name = input()

command = input()

while not command == "End":
    if command.startswith("refill"):
        liters_to_add = int(command.split()[1])
        water_qt += liters_to_add
    else:
        liters_to_get = int(command)
        if liters_to_get <= water_qt:
            water_qt -= liters_to_get
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")

    command = input()

print(f"{water_qt} liters left")