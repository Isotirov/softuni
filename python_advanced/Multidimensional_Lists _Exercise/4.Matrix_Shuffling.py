# rows, cols = [int(x) for x in input().split()]
#
# matrix = []
#
# for row in range(rows):
#     matrix.append([x for x in input().split()])
#
# command = input()
#
# while not command == "END":
#     if "swap" in command:
#         current_command = command.split()
#         if len(current_command) == 5:
#             row = int(current_command[1])
#             col = int(current_command[2])
#             row_rep = int(current_command[3])
#             col_rep = int(current_command[4])
#             if 0 <= row < rows and 0 <= row_rep < rows and 0 <= col < cols and 0 <= col_rep < cols:
#                 matrix[row][col], matrix[row_rep][col_rep] = matrix[row_rep][col_rep], matrix[row][col]
#                 for r in range(rows):
#                     print(' '.join(matrix[r]))
#             else:
#                 print("Invalid input!")
#         else:
#             print("Invalid input!")
#     else:
#         print("Invalid input!")
#
#     command = input()


def index_check_row(value):
    if 0 <= value < len(matrix):
        return True
    return False


def index_check_column(value):
    if 0 <= value < len(matrix[0]):
        return True
    return False


n, m = [int(x) for x in input().split()]

matrix = []

for r in range(n):
    matrix.append([x for x in input().split()])

command = input()

while not command == "END":
    is_valid = False
    if "swap" in command:
        current_command = command.split()
        if len(current_command) == 5:
            r1, r2 = int(current_command[1]), int(current_command[3])
            c1, c2 = int(current_command[2]), int(current_command[4])
            if index_check_row(r1) and index_check_row(r2) and index_check_column(c1) and index_check_column(c2):
                matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
                is_valid = True

    if is_valid:
        for r in range(n):
            print(" ".join(x for x in matrix[r]))
    else:
        print("Invalid input!")

    command = input()