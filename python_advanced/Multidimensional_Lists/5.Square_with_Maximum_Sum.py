# import sys
#
# rows, cols = [int(x) for x in input().split(", ")]
#
# matrix = []
# max_sum = -sys.maxsize
# position = None
#
# for row in range(rows):
#     matrix.append([int(x) for x in input().split(", ")])
#
# for row in range(rows-1, 0, -1):
#     for col in range(cols-1, 0, -1):
#         current_sum = 0
#         current_sum += matrix[row][col] + matrix[row][col-1] + matrix[row-1][col] + matrix[row-1][col-1]
#         if current_sum >= max_sum:
#             max_sum = current_sum
#             position = (row, col)
#             # elements_1 = (matrix[row-1][col-1], matrix[row-1][col])
#             # elements_2 = (matrix[row][col-1], matrix[row][col])
#
# r, c = position
# # print(*elements_1)
# # print(*elements_2)
# print(matrix[r-1][c-1], matrix[r-1][c])
# print(matrix[r][c-1], matrix[r][c])
# print(max_sum)


n, m = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(", ")])

maximum_sum = 0
first = ()
second = ()

for r in range(n-1):
    current_sum = 0
    for c in range(m-1):
        current_sum = matrix[r][c] + matrix[r][c+1] + matrix[r+1][c] + matrix[r+1][c+1]
        if current_sum > maximum_sum:
            maximum_sum = current_sum
            first = (matrix[r][c], matrix[r][c+1])
            second = (matrix[r+1][c], matrix[r+1][c+1])

print(*first)
print(*second)
print(maximum_sum)