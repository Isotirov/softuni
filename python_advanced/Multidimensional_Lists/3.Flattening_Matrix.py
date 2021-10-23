n = int(input())

matrix = []

for r in range(n):
    matrix.append([int(x) for x in input().split(", ")])

flattened_matrix = [c for r in matrix for c in r]
print(flattened_matrix)