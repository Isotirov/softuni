rows, cols = [int(x) for x in input().split(", ")]

matrix = []
total = 0

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])
    total += sum(matrix[row])

print(total)
print(matrix)