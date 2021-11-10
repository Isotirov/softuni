# rows, cols = [int(x) for x in input().split()]
#
# matrix = []
# snake = list(input())
#
# for row in range(rows):
#     matrix.append([])
#     for col in range(cols):
#         if row % 2 == 0:
#             matrix[row].append(snake[0])
#         else:
#             matrix[row].insert(0, snake[0])
#         snake.append(snake.pop(0))
#     print(''.join(matrix[row]))


from collections import deque

n, m = [int(x) for x in input().split()]

snake = deque(input())

matrix = []

for r in range(n):
    matrix.append([])
    if r % 2 == 0:
        for c in range(m):
            matrix[r].append(snake[0])
            snake.append(snake.popleft())
    else:
        for c in range(m):
            matrix[r].insert(0, snake[0])
            snake.append(snake.popleft())

for r in range(n):
    print(''.join(matrix[r]))