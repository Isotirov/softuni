def valid_checker(r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False


matrix = [[int(j) for j in input().split()] for r in range(int(input()))]

command = input()

while not command == "END":
    current_data = command.split()
    to_do = current_data[0]
    row = int(current_data[1])
    col = int(current_data[2])
    value = int(current_data[3])

    if valid_checker(row, col):
        if to_do == "Add":
            matrix[row][col] += value
        elif to_do == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

    command = input()

[print(' '.join(str(x) for x in matrix[r])) for r in range(len(matrix))]