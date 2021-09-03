legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
items = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}

is_crafted = False
crafted_item = ""

while True:
    if is_crafted:
        break

    data = input().split()
    for x in range(0, len(data), 2):
        qt = int(data[x])
        item = data[x+1].lower()
        if item in items:
            items[item] += qt
            if items[item] >= 250:
                items[item] -= 250
                is_crafted = True
                crafted_item = item
                break
        else:
            if item not in junk_items:
                junk_items[item] = qt
            else:
                junk_items[item] += qt

print(f"{legendary_items[crafted_item]} obtained!")

sorted_items = dict(sorted(items.items(), key=lambda kvp: (-kvp[1], kvp[0])))
for key, value in sorted_items.items():
    print(f"{key}: {value}")
junk_sort = dict(sorted(junk_items.items(), key=lambda kvp: kvp[0]))
for key, value in junk_sort.items():
    print(f"{key}: {value}")