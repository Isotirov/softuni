from collections import deque

line = input()

customers = deque()

while not line == "End":
    if line == "Paid":
        while customers:
            print(customers.popleft())
    else:
        customers.append(line)

    line = input()

print(f"{len(customers)} people remaining.")