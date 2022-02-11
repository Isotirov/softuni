def movement(rw, cw, where):
    somewhere = {
        "up": (rw - 1, cw),
        "down": (rw + 1, cw),
        "left": (rw, cw - 1),
        "right": (rw, cw + 1)
    }
    return somewhere[where]


def valid_check(rw, cw):
    if 0 <= rw < len(matrix) and 0 <= cw < len(matrix):
        return True
    return False


n = int(input())

# matrix = [[x for x in input().split()] for r in range(n)]

matrix = []
bunny = ()

for r in range(n):
    rows = input().split()
    matrix.append(rows)
    for c in range(n):
        el = rows[c]
        if el == "B":
            bunny = (r, c)
            break

max_eggs = float("-inf")
locations = []
direction = ""

directions = "up", "down", "left", "right"

for side in directions:
    bunny_row, bunny_col = bunny
    eggs = 0
    current_locations = []
    while True:
        bunny_row, bunny_col = movement(bunny_row, bunny_col, side)
        if not valid_check(bunny_row, bunny_col):
            break
        else:
            if matrix[bunny_row][bunny_col] == "X":
                break
            else:
                eggs += int(matrix[bunny_row][bunny_col])
                current_locations.append([bunny_row, bunny_col])

    if eggs >= max_eggs:
        max_eggs = eggs
        locations = current_locations
        direction = side


print(direction)
for x in locations:
    print(x)
print(max_eggs)
