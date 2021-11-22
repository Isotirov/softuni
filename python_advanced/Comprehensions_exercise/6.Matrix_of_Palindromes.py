r, c = [int(x) for x in input().split()]

matrix = [[f'{chr(97+row) + chr(97+row+col) + chr(97+row)}' for col in range(c)] for row in range(r)]

[print(' '.join(matrix[row])) for row in range(r)]