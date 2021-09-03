country_names = input().split(", ")
capital = input().split(", ")

capitals = dict(zip(country_names, capital))

for city, cap in capitals.items():
    print(f"{city} -> {cap}")