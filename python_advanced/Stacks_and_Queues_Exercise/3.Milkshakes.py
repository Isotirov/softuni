from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque(int(x) for x in input().split(", "))
milkshakes = 0

while chocolates and cups_of_milk:
    if milkshakes == 5:
        break

    choc = chocolates.pop()
    milk = cups_of_milk.popleft()

    if choc <= 0 and milk <= 0:
        continue
    if choc <= 0:
        cups_of_milk.appendleft(milk)
        continue
    if milk <= 0:
        chocolates.append(choc)
        continue

    if choc == milk:
        milkshakes += 1

    else:
        cups_of_milk.append(milk)
        choc -= 5
        chocolates.append(choc)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print("Chocolate: ", end="")
    print(*chocolates, sep=", ")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print("Milk: ", end="")
    print(*cups_of_milk, sep=", ")
else:
    print("Milk: empty")