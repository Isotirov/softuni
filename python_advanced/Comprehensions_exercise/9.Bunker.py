item_categories = input().split(", ")

n = int(input())

dictionary = {item: [] for item in item_categories}
dict_qt = []
dict_quality = []

for _ in range(n):
    category, item, data = input().split(" - ")
    item_quantity_data, item_quality_data = data.split(";")
    item_quantity = int(item_quantity_data.split(":")[1])
    item_quality = int(item_quality_data.split(":")[1])
    dictionary[category].append(item)
    dict_qt.append(item_quantity)
    dict_quality.append(item_quality)

print(f"Count of items: {sum(dict_qt)}")
print(f"Average quality: {sum(dict_quality) / len(dictionary):.2f}")

print('\n'.join(f"{item} -> {', '.join(value)}" for item, value in dictionary.items()))