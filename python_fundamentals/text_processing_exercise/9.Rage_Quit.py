data = input()

to_repeat = ""
result = ""
number = ""
i = 0

while i < len(data):
    if not data[i].isdigit():
        to_repeat += data[i]
        i += 1
    elif data[i].isdigit():

        while data[i].isdigit():
            number += data[i]
            i += 1
            if i == len(data):
                break
        number = int(number)
        result += to_repeat.upper() * number
        to_repeat = ""
        number = ""

print(f"Unique symbols used: {len(set(result))}")
print(result)