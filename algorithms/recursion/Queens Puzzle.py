matrix = []

for _ in range(8):
    matrix.append(['-'] * 8)

rows = set()
cols = set()
left_diag = set()
right_diag = set()


def can_place(r, c):
    if r in rows or c in cols or c-r in left_diag or c+r in right_diag:
        return False
    return True


def set_queen(r, c, lab):
    lab[r][c] = '*'
    rows.add(r)
    cols.add(c)
    left_diag.add(c-r)
    right_diag.add(c+r)


def remove_queen(r, c, lab):
    lab[r][c] = '-'
    rows.remove(r)
    cols.remove(c)
    left_diag.remove(c - r)
    right_diag.remove(c + r)


def print_board(lab):
    for r in lab:
        print(' '.join(r))
    print()


def queens(r, lab):
    if r == 8:
        print_board(lab)
        return
    for c in range(8):
        if can_place(r, c):
            set_queen(r, c, lab)
            queens(r+1, lab)
            remove_queen(r, c, lab)


queens(0, matrix)
