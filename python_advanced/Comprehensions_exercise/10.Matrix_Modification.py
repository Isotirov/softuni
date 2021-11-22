def valid_check(r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False


matrix = [[int(col) for col in input().split()] for row in range(int(input()))]

command = input()

while not command == "END":
    to_do, row, col, value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if valid_check(row, col):
        if to_do == "Add":
            matrix[row][col] += value
        elif to_do == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

    command = input()

[print(' '.join(str(x) for x in row)) for row in matrix]