def valid_check(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


n = int(input())

matrix = []
alice = ()


for r in range(n):
    elements = input().split()
    matrix.append(elements)
    for c in range(n):
        if matrix[r][c] == "A":
            alice = (r, c)
            break

command = input()
row, col = alice
matrix[row][col] = "*"
tea = 0

while command:

    directions = {
        "up": (row - 1, col),
        "down": (row + 1, col),
        "left": (row, col - 1),
        "right": (row, col + 1)
    }
    row, col = directions[command]
    if valid_check(row, col):
        if matrix[row][col] == "R":
            matrix[row][col] = "*"
            break
        else:
            if not matrix[row][col] == "." and not matrix[row][col] == "*":
                tea += int(matrix[row][col])
            matrix[row][col] = "*"
    else:
        break
    if tea >= 10:
        break
    command = input()

if tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(' '.join(x for x in matrix[r])) for r in range(len(matrix))]