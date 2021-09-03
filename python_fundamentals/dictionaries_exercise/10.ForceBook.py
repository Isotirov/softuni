def find_user(diction, user):
    found = False
    for value in diction.values():
        if user in value:
            found = True
    return found


data = input()

force_place = {}

while not data == "Lumpawaroo":
    if "|" in data:
        current_data = data.split(" | ")
        force_side = current_data[0]
        force_user = current_data[1]
        if not find_user(force_place, force_user) and force_side not in force_place:
            force_place[force_side] = [force_user]
        elif not find_user(force_place, force_user):
            force_place[force_side].append(force_user)
    else:
        current_data = data.split(" -> ")
        force_side = current_data[1]
        force_user = current_data[0]
        if find_user(force_place, force_user):
            for k, v in force_place.items():
                for item in v:
                    if item == force_user:
                        v.remove(force_user)
            if force_side not in force_place:
                force_place[force_side] = [force_user]
            else:
                force_place[force_side].append(force_user)
        elif not find_user(force_place, force_user):
            if force_side not in force_place:
                force_place[force_side] = [force_user]
            else:
                force_place[force_side].append(force_user)
        if not find_user(force_place, force_user) and force_side not in force_place:
            force_place[force_side] = [force_user]
        print(f"{force_user} joins the {force_side} side!")
    data = input()

for_print = sorted(force_place.items(), key=lambda x: (-len(x[1]), x[0]))
for side, member in for_print:
    if len(member):
        print(f"Side: {side}, Members: {len(member)}")
        member = sorted(member)
        for x in member:
            print(f"! {x}")