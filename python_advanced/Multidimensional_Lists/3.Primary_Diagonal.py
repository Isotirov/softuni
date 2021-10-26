rows = int(input())

matrix = []
total = 0

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows):
    for col in range(rows):
        if row == col:
            total += matrix[row][col]
print(total)