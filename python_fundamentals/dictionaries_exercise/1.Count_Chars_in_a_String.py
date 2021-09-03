string = input()

diction = {}

for char in string:
    if not char == " " and char not in diction:
        diction[char] = 1
    elif not char == " " and char in diction:
        diction[char] += 1

for key, value in diction.items():
    print(f"{key} -> {value}")