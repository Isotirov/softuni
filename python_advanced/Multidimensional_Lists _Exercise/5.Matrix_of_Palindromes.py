n, m = [int(x) for x in input().split()]

matrix = []
letter = 97

for r in range(n):
    matrix.append([])
    for c in range(m):
        matrix[r].append(chr(letter+r) + chr(letter+r+c) + chr(letter+r))

for r in range(n):
    print(' '.join(matrix[r]))