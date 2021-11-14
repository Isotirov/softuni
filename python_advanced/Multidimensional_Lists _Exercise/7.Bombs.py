# rows = int(input())
#
# matrix = []
#
# # matrix creation
# for row in range(rows):
#     matrix.append([int(x) for x in input().split()])
#
# # list with bombs
# bombs = input().split()
#
#
# for bomb in bombs:
#     current_bomb = bomb.split(",")
#     row = int(current_bomb[0])
#     col = int(current_bomb[1])
#     if matrix[row][col] <= 0:
#         continue
#     bomb_power = matrix[row][col]
#     matrix[row][col] = 0
#
#     # cells around the bomb
#     cells = [
#         (row-1, col-1),
#         (row-1, col),
#         (row-1, col+1),
#         (row, col-1),
#         (row, col+1),
#         (row+1, col-1),
#         (row+1, col),
#         (row+1, col+1)
#     ]
#
#     # damaging the cells around the bomb
#     for cell in cells:
#         row, col = cell
#         if 0 <= row < len(matrix) and 0 <= col < len(matrix):
#             if matrix[row][col] > 0:
#                 matrix[row][col] -= bomb_power
#
# count = 0
# total = 0
#
# for row in range(rows):
#     for col in range(rows):
#         if matrix[row][col] > 0:
#             count += 1
#             total += matrix[row][col]
#
# print(f"Alive cells: {count}")
# print(f"Sum: {total}")
#
# for row in range(rows):
#     print(*matrix[row])


def checker(value):
    for i in value:
        if 0 <= i < len(matrix):
            continue
        else:
            return False
    return True


n = int(input())

matrix = []

for r in range(n):
    matrix.append([int(x) for x in input().split()])


bombs = input().split()

for bomb in bombs:
    row, col = bomb.split(",")
    row = int(row)
    col = int(col)
    if matrix[row][col] <= 0:
        continue
    bomb_power = matrix[row][col]
    matrix[row][col] = 0

    possible_booms = [
        (row - 1, col),
        (row - 1, col-1),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col),
        (row + 1, col - 1),
        (row + 1, col + 1)
    ]

    for boom in possible_booms:
        if checker(boom):
            row, col = boom
            if not matrix[row][col] <= 0:
                matrix[row][col] -= bomb_power

alive = [c for r in matrix for c in r if c > 0]

print(f"Alive cells: {len(alive)}")
print(f"Sum: {sum(alive)}")
[print(' '.join(str(x) for x in matrix[r])) for r in range(len(matrix))]