def attack(r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False


matrix = [[x for x in input()] for r in range(int(input()))]

knights = [(r, x) for r in range(len(matrix)) for x in range(len(matrix[r])) if matrix[r][x] == "K"]

count = 0

while knights:
    madness = 0
    hooligan = ()
    for knight in knights:
        aggressive = 0
        row, col = knight

        attack_moves = [
            (row - 1, col - 2),
            (row - 2, col - 1),
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col - 2),
            (row + 2, col - 1),
            (row + 2, col + 1),
            (row + 1, col + 2)
        ]

        for fight in attack_moves:
            row, col = fight
            if attack(row, col):
                if matrix[row][col] == "K":
                    aggressive += 1
        if aggressive > madness:
            madness = aggressive
            hooligan = knight
    if hooligan:
        matrix[hooligan[0]][hooligan[1]] = "0"
        knights.remove(hooligan)
        count += 1
        continue
    break

print(count)