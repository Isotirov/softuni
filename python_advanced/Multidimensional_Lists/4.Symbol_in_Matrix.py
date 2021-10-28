rows = int(input())

matrix = []
position = None

for row in range(rows):
    matrix.append(list(input()))

symbol = input()

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == symbol:
            position = (row, col)
            break
    if position:
        break

print(position if position else f"{symbol} does not occur in the matrix")