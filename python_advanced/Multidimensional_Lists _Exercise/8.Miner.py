# def valid_move(r, c):
#     if 0 <= r < len(matrix) and 0 <= c < len(matrix):
#         return True
#     else:
#         return False
#
#
# rows = int(input())
# moves = input().split()
#
# matrix = []
#
# for row in range(rows):
#     matrix.append([x for x in input().split()])
#
# coals = []
# start = ()
# coal_count = 0
# end = False
#
# for row in range(rows):
#     for col in range(rows):
#         if matrix[row][col] == "c":
#             coals.append((row, col))
#         elif matrix[row][col] == "s":
#             start = (row, col)
#
# row, col = start
# for move in moves:
#     if move == "up":
#         row -= 1
#         if not valid_move(row, col):
#             row += 1
#             continue
#     elif move == "down":
#         row += 1
#         if not valid_move(row, col):
#             row -= 1
#             continue
#     elif move == "left":
#         col -= 1
#         if not valid_move(row, col):
#             col += 1
#             continue
#     elif move == "right":
#         col += 1
#         if not valid_move(row, col):
#             col -= 1
#             continue
#     if matrix[row][col] == "c":
#         coal_count += 1
#         matrix[row][col] = "*"
#         coals.remove((row, col))
#         if not coals:
#             print(f"You collected all coals! {row, col}")
#             end = True
#             break
#     elif matrix[row][col] == "e":
#         print(f"Game over! {row, col}")
#         end = True
#         break
#
# if not end:
#     print(f"{len(coals)} coals left. ({row}, {col})")


def checker(value):
    for i in value:
        if not 0 <= i < len(matrix):
            return False
    return True


n = int(input())

commands = input().split()

matrix = []

for r in range(n):
    matrix.append(input().split())

coals = []
miner = ()
end = ()

for r in range(n):
    for c in range(n):
        if matrix[r][c] == "c":
            coals.append((r, c))
        elif matrix[r][c] == "s":
            miner = (r, c)
        elif matrix[r][c] == "e":
            end = (r, c)

row, col = miner
game_over = False

for command in commands:

    moves = {
        "left": (row, col - 1),
        "right": (row, col + 1),
        "up": (row - 1, col),
        "down": (row + 1, col)
    }

    if checker(moves[command]):
        row = moves[command][0]
        col = moves[command][1]
        current_cell = matrix[row][col]
        if current_cell == "e":
            print(f"Game over! ({row}, {col})")
            game_over = True
            break
        elif current_cell == "c":
            matrix[row][col] = "*"
            coals.remove((row, col))
            if not coals:
                print(f"You collected all coal! ({row}, {col})")
                break

if not game_over:
    if coals:
        print(f"{len(coals)} pieces of coal left. ({row}, {col})")