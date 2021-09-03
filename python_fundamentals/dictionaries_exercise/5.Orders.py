data = input()

price_dict = {}
qt_dict = {}

while not data == "buy":
    current_data = data.split()
    item_name = current_data[0]
    price = float(current_data[1])
    qt = int(current_data[2])

    price_dict[item_name] = price

    if item_name not in qt_dict:
        qt_dict[item_name] = 0
    qt_dict[item_name] += qt

    data = input()

for key, value in price_dict.items():
    print(f"{key} -> {value * qt_dict[key]:.2f}")