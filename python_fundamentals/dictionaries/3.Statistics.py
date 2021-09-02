command = input()

stat_list = {}

while not command == "statistics":
    key, value = command.split(": ")
    if key in stat_list:
        stat_list[key] += int(value)
    else:
        stat_list[key] = int(value)
    command = input()

print("Products in stock:")
for key, value in stat_list.items():
    print(f"- {key}: {stat_list[key]}")

print(f"Total Products: {len(stat_list)}")
sum_values = sum(stat_list.values())
print(f"Total Quantity: {sum_values}")