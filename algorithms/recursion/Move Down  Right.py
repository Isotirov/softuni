# rows = int(input())
# cols = int(input())
#
# counter = 0
#
#
# def paths(r, c, row, col, count):
#     if r < 0 or r >= row or c > 0 or c >= col:
#         return 0
#     if r == row-1 and c == col - 1:
#         return 1
#     count += paths(r + 1, c, row, col, count)
#     count += paths(r, c + 1, row, col, count)
#
#
# paths(0, 0, rows, cols, counter)
# print(counter)
#


rows = int(input())
cols = int(input())

count = []


def move(r, c, count):
    if r < 0 or c < 0 or r >= rows or c >= cols:
        return
    if r == rows - 1 and c == cols - 1:
        count.append(1)
        return

    move(r + 1, c, count)
    move(r, c + 1, count)


move(0, 0, count)
print(len(count))
