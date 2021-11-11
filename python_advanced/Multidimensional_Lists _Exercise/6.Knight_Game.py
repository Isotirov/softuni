rows = int(input())

matrix = []
knights = []
count = 0

for row in range(rows):
    current_row = list(input())
    matrix.append([])
    for el in current_row:
        matrix[row].append(el)
        if el == "K":
            knights.append((row, len(matrix[row])-1))

while knights:
    max_aggressive = 0
    knight_to_remove = ()
    for knight in knights:
        aggressive = 0
        row, col = knight
        possible_moves = [
            (row-1, col-2),
            (row-2, col-1),
            (row-2, col+1),
            (row-1, col+2),
            (row+1, col+2),
            (row+2, col+1),
            (row+2, col-1),
            (row+1, col-2)
        ]

        for move in possible_moves:
            row, col = move
            if 0 <= row < len(matrix) and 0 <= col < len(matrix):
                if matrix[row][col] == "K":
                    aggressive += 1
        if aggressive > max_aggressive:
            max_aggressive = aggressive
            knight_to_remove = knight

    if knight_to_remove:
        row, col = knight_to_remove
        matrix[row][col] = "0"
        knights.remove(knight_to_remove)
        count += 1
        continue

    break

print(count)