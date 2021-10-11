from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

toys = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}

while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()
    result = current_material * current_magic
    if current_material == 0 and current_magic == 0:
        continue
    elif current_material == 0:
        magic_level.appendleft(current_magic)
        continue
    elif current_magic == 0:
        materials.append(current_material)
        continue
    if result == 150:
        toys["Doll"] += 1
    elif result == 250:
        toys["Wooden train"] += 1
    elif result == 300:
        toys["Teddy bear"] += 1
    elif result == 400:
        toys["Bicycle"] += 1

    else:
        if result < 0:
            sum_values = current_material + current_magic
            materials.append(sum_values)
        elif result > 0:
            materials.append(current_material + 15)

if toys["Doll"] >= 1 and toys["Wooden train"] >= 1:
    print("The presents are crafted! Merry Christmas!")
if toys["Teddy bear"] >= 1 and toys["Bicycle"] >= 1:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")
#
# for key, value in sorted(toys.items()):
#     print(f"{key}: {value}")

[print(f"{key}: {value}") for key, value in sorted(toys.items()) if value > 0]