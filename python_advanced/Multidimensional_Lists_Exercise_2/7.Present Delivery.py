def movement(grandpa, move):
    rw, cw = grandpa

    somewhere = {
        "up": (rw - 1, cw),
        "down": (rw + 1, cw),
        "left": (rw, cw - 1),
        "right": (rw, cw + 1)
    }
    return somewhere[move]


def valid_move(rw, cw):
    if 0 <= rw < n and 0 <= cw < n:
        return True
    return False


santa_presents = int(input())

n = int(input())

matrix = []
santa = ()
good_kids = []

for r in range(n):
    houses = input().split()
    matrix.append(houses)
    for c in range(n):
        if matrix[r][c] == "S":
            santa = r, c
        elif matrix[r][c] == "V":
            good_kids.append((r, c))

count_good_kids = len(good_kids)

command = input()

while not command == "Christmas morning":
    santa_row, santa_col = movement(santa, command)

    if valid_move(santa_row, santa_col):
        if matrix[santa_row][santa_col] == "V":
            santa_presents -= 1
            good_kids.remove((santa_row, santa_col))
            matrix[santa_row][santa_col] = "S"
            matrix[santa[0]][santa[1]] = "-"
            santa = santa_row, santa_col

        elif matrix[santa_row][santa_col] == "C":
            matrix[santa_row][santa_col] = "S"
            matrix[santa[0]][santa[1]] = "-"
            santa = santa_row, santa_col
            directions = ["left", "right", "up", "down"]
            for direct in directions:
                row, col = movement(santa, direct)
                if valid_move(row, col):
                    if matrix[row][col] == "V":
                        if santa_presents:
                            santa_presents -= 1
                            good_kids.remove((row, col))
                            matrix[row][col] = "-"
                    elif matrix[row][col] == "X":
                        if santa_presents:
                            santa_presents -= 1
                            matrix[row][col] = "-"
                    else:
                        continue
        else:
            matrix[santa_row][santa_col] = "S"
            matrix[santa[0]][santa[1]] = "-"
            santa = santa_row, santa_col

    if not santa_presents:
        break

    command = input()

if not santa_presents and good_kids:
    print("Santa ran out of presents!")
[print(' '.join(x for x in matrix[r])) for r in range(n)]
if not good_kids:
    print(f"Good job, Santa! {count_good_kids} happy nice kid/s.")
else:
    print(f'No presents for {len(good_kids)} nice kid/s.')