# import sys
#
# rows, cols = [int(x) for x in input().split()]
#
# matrix = []
# maximal = -sys.maxsize
# position = None
#
# for row in range(rows):
#     matrix.append([int(x) for x in input().split()])
#
# for row in range(rows - 2):
#     for col in range(cols - 2):
#         current_sum = 0
#         current_sum += matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
#                        matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
#                        matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
#         if current_sum > maximal:
#             maximal = current_sum
#             position = (row, col)
#
# r, c = position
# print(f"Sum = {maximal}")
# print(matrix[r][c], matrix[r][c + 1], matrix[r][c + 2])
# print(matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2])
# print(matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2])


import sys

n, m = [int(x) for x in input().split()]

matrix = []

for r in range(n):
    matrix.append([int(x) for x in input().split()])

maximal_sum = -sys.maxsize
first = ()
second = ()
third = ()

for r in range(n - 2):
    current_sum = 0
    for c in range(m - 2):
        current_sum = matrix[r][c] + \
                      matrix[r][c + 1] + \
                      matrix[r][c + 2] + \
                      matrix[r + 1][c] + \
                      matrix[r + 1][c + 1] + \
                      matrix[r + 1][c + 2] + \
                      matrix[r + 2][c] + \
                      matrix[r + 2][c + 1] + \
                      matrix[r + 2][c + 2]
        if current_sum > maximal_sum:
            maximal_sum = current_sum
            first = (matrix[r][c], matrix[r][c + 1], matrix[r][c + 2])
            second = (matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2])
            third = (matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2])

print(f"Sum = {maximal_sum}")
print(*first, sep=" ")
print(*second, sep=" ")
print(*third, sep=" ")