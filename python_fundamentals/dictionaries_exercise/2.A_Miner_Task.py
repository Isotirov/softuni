diction = {}

while True:
    resource = input()
    if resource == "stop":
        break
    qt = int(input())
    if resource not in diction:
        diction[resource] = qt
    else:
        diction[resource] += qt
for key, value in diction.items():
    print(f"{key} -> {value}")