# def valid_move(r, c):
#     if 0 <= r < rows and 0 <= c < cols:
#         return True
#     return False
#
#
# def multiply_bunnies(buns):
#     for bunny in buns:
#         r, c = bunny
#         possible_spread = [
#             (r + 1, c),
#             (r - 1, c),
#             (r, c + 1),
#             (r, c - 1)
#         ]
#         for spread in possible_spread:
#             r, c = spread
#             if valid_move(r, c):
#                 matrix[r][c] = "B"
#     return matrix
#
#
# rows, cols = [int(x) for x in input().split()]
#
# matrix = []
#
# for row in range(rows):
#     matrix.append([x for x in input()])
#
# moves = [x for x in input()]
# bunnies = []
# player = ()
# won = True
#
# for row in range(rows):
#     for col in range(cols):
#         if matrix[row][col] == "P":
#             player = (row, col)
#             break
#
# for move in moves:
#     for row in range(rows):
#         for col in range(cols):
#             if matrix[row][col] == "B":
#                 bunnies.append((row, col))
#     row, col = player
#     if matrix[row][col] == "B":
#         won = False
#         break
#
#     if move == "L":
#         col -= 1
#     elif move == "R":
#         col += 1
#     elif move == "U":
#         row -= 1
#     elif move == "D":
#         row += 1
#     if valid_move(row, col):
#         if matrix[row][col] == "B":
#             won = False
#             player = (row, col)
#             matrix = multiply_bunnies(bunnies)
#             break
#         else:
#             matrix[player[0]][player[1]] = "."
#             matrix[row][col] = "P"
#             player = (row, col)
#             matrix = multiply_bunnies(bunnies)
#     elif not valid_move(row, col):
#         matrix[player[0]][player[1]] = "."
#         matrix = multiply_bunnies(bunnies)
#         break
#
# for row in range(rows):
#     print(''.join(matrix[row]))
#
# if won:
#     print(f"won: {player[0]} {player[1]}")
# else:
#     print(f"dead: {player[0]} {player[1]}")


def move_checker(value):
    r1, c1 = value
    if 0 <= r1 < n and 0 <= c1 < m:
        return True
    return False


n, m = [int(x) for x in input().split()]

matrix = []

for r in range(n):
    matrix.append([x for x in input()])

moves = [x for x in input()]

player = ()

for r in range(n):
    for c in range(m):
        if matrix[r][c] == "P":
            player = (r, c)
            break

win = False
eaten = False


for move in moves:
    row, col = player

    commands = {
        "U": (row - 1, col),
        "D": (row + 1, col),
        "L": (row, col - 1),
        "R": (row, col + 1)
    }

    matrix[row][col] = "."
    if not move_checker(commands[move]):
        win = True
    else:
        row = commands[move][0]
        col = commands[move][1]
        if matrix[row][col] == "B":
            eaten = True
        else:
            matrix[row][col] = "P"
        player = (row, col)

    bunnies = []
    [bunnies.append((r, c)) for r in range(n) for c in range(m) if matrix[r][c] == "B"]

    for bunny in bunnies:
        b_row, b_col = bunny

        spread = [
            (b_row, b_col + 1),
            (b_row, b_col - 1),
            (b_row + 1, b_col),
            (b_row - 1, b_col)
        ]

        for s in spread:
            b_row, b_col = s
            if move_checker(s):
                if matrix[b_row][b_col] == "P":
                    eaten = True
                matrix[b_row][b_col] = "B"

    if eaten or win:
        break

[print(''.join(matrix[r])) for r in range(n)]

if win:
    print(f"won: {player[0]} {player[1]}")
else:
    print(f"dead: {player[0]} {player[1]}")