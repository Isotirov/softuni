rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

sum_first_diagonal = 0
sum_second_diagonal = 0

for first in range(rows):
    sum_first_diagonal += matrix[first][first]

col = rows
for second in range(rows):
    col -= 1
    sum_second_diagonal += matrix[second][col]

print(abs(sum_first_diagonal - sum_second_diagonal))