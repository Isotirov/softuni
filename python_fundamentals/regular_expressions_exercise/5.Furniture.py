import re

furniture = input()
pattern = r">>(?P<furniture>[A-Za-z]+(_[A-Za-z])*)<<(?P<price>\d+(\.\d+)*)!(?P<qt>\d+)"
money = 0
bought_furniture = []

while not furniture == "Purchase":
    match = re.finditer(pattern, furniture)
    if match:
        for group in match:
            money += float(group.group("price")) * int(group.group("qt"))
            bought_furniture.append(group.group("furniture"))
    furniture = input()

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {money:.2f}")
