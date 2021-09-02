data = input().split()

food = {}

for ind in range(0, len(data), 2):
    product = data[ind]
    qt = int(data[ind+1])
    food[product] = qt

print(food)