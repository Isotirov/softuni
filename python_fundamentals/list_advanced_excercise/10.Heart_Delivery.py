neighborhood = [int(x) for x in input().split("@")]

command = input()
start = 0

while not command == "Love!":
    jump = int(command.split()[1])
    start += jump
    if start >= len(neighborhood):
        start = 0
    if neighborhood[start] > 0:
        neighborhood[start] -= 2
        if neighborhood[start] == 0:
            print(f"Place {start} has Valentine's day.")
    else:
        print(f"Place {start} already had Valentine's day.")
    command = input()
print(f"Cupid's last position was {start}.")
valentine = [x for x in neighborhood if not x == 0]
if valentine:
    print(f"Cupid has failed {len(valentine)} places.")
else:
    print("Mission was successful.")