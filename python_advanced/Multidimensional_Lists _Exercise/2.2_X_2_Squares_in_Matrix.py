rows, cols = [int(x) for x in input().split()]

matrix = []
match = 0

for row in range(rows):
    matrix.append([x for x in input().split()])

for row in range(0, rows - 1):
    for col in range(0, cols - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            match += 1

print(match)
