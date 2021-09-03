data = input()

diction = {}

while not data == "buy":
    name, price, qt = data.split()
    price = float(price)
    qt = int(qt)
    if name not in diction:
        diction[name] = {"price": price, "qt": qt}
    else:
        diction[name]["price"] = price
        diction[name]["qt"] += qt
    data = input()

for product, cost in diction.items():
    print(f"{product} -> {cost['price'] * cost['qt']:.2f}")