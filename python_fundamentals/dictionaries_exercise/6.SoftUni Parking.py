n = int(input())

registered = {}

for _ in range(n):
    command = input().split()
    name = command[1]
    if command[0] == "register":
        licenses = command[2]
        if name in registered:
            registered[name] = licenses
            print(f"ERROR: already registered with plate number {registered[name]}")
        else:
            registered[name] = licenses
            print(f"{name} registered {licenses} successfully")
    elif command[0] == "unregister":
        if name not in registered:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            registered.pop(name)

for key, value in registered.items():
    print(f"{key} => {value}")