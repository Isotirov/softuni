def go(pos, direct, step):
    rw, cl = pos

    transit = {"up": (rw - step, cl),
               "down": (rw + step, cl),
               "left": (rw, cl - step),
               "right": (rw, cl + step)
               }
    return transit[direct]


def validate_position(rw, cw):
    if 0 <= rw < n and 0 <= cw < n:
        return True
    return False


n = 5

matrix = []
player = ()

targets = 0
shot_targets = 0
shot_targets_location = []

for r in range(n):
    elements = input().split()
    matrix.append(elements)
    for c in range(n):
        if matrix[r][c] == "A":
            player = (r, c)
        elif matrix[r][c] == "x":
            targets += 1

commands_n = int(input())

for _ in range(commands_n):
    command = input().split()
    action = command[0]
    direction = command[1]

    if action == "move":
        steps = int(command[2])

        row, col = player
        d_row, d_col = go(player, direction, steps)
        if not validate_position(d_row, d_col):
            continue
        else:
            if matrix[d_row][d_col] == ".":
                matrix[row][col] = "."
                matrix[d_row][d_col] = "A"
                player = d_row, d_col
            else:
                continue

    elif action == "shoot":
        bullet_move = player
        while True:

            d_row, d_col = go(bullet_move, direction, 1)
            if not validate_position(d_row, d_col):
                break
            else:
                if matrix[d_row][d_col] == "x":
                    matrix[d_row][d_col] = "."
                    shot_targets += 1
                    targets -= 1
                    shot_targets_location.append([d_row, d_col])
                    break
            bullet_move = d_row, d_col
    if not targets:
        break


if not targets and shot_targets:
    print(f"Training completed! All {shot_targets} targets hit.")
else:
    if targets:
        print(f"Training not completed! {targets} targets left.")
for target in shot_targets_location:
    print(target)
