heroes_names = input().split(", ")

command = input()
dictionary = {hero: {} for hero in heroes_names}

while not command == "End":
    name, item, cost = command.split("-")
    cost = int(cost)
    # if name not in dictionary:
    #     dictionary[name] = {"item": [], "cost": 0}
    if item not in dictionary[name]:
        dictionary[name][item] = cost

    command = input()

print('\n'.join(f"{hero} -> Items: {len(dictionary[hero])}, Cost: {sum(dictionary[hero].values())}" for hero in heroes_names))