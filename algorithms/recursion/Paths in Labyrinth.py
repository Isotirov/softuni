row = int(input())
col = int(input())

matrix = []

for _ in range(row):
    matrix.append(list(input()))


def find_path(r, c, lab, direction, path):
    if r < 0 or r >= len(lab) or c < 0 or c >= len(lab[0]):
        return
    if lab[r][c] == '*':
        return
    if lab[r][c] == 'v':
        return

    path.append(direction)

    if lab[r][c] == 'e':
        print(''.join(path))
    else:
        lab[r][c] = 'v'

        find_path(r + 1, c, lab, 'D', path)
        find_path(r, c + 1, lab, 'R', path)
        find_path(r - 1, c, lab, 'U', path)
        find_path(r, c - 1, lab, 'L', path)

        lab[r][c] = '-'

    path.pop()


find_path(0, 0, matrix, '', [])
