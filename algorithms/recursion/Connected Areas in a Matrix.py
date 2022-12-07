# rows = int(input())
# cols = int(input())
#
# matrix = []
#
# for _ in range(rows):
#     matrix.append(list(input()))
#
#
# def connections(r, c, lab):
#     if r < 0 or c < 0 or r >= len(lab) or c >= len(lab[0]):
#         return 0
#     if lab[r][c] != '-':
#         return 0
#     lab[r][c] = 'v'
#
#     result = 1
#
#     result += connections(r + 1, c, lab)
#     result += connections(r, c + 1, lab)
#     result += connections(r - 1, c, lab)
#     result += connections(r, c - 1, lab)
#
#     return result
#
#
# results = []
#
# for row in range(rows):
#     for col in range(cols):
#         curr_result = connections(row, col, matrix)
#         if curr_result != 0:
#             results.append((row, col, curr_result))
#
# sorted_for_print = sorted(results, key=lambda x: (-x[2], x[1], x[0]))
#
# print(f'Total areas found: {len(sorted_for_print)}')
# for i in range(len(sorted_for_print)):
#     print(f'Area #{i+1} at ({sorted_for_print[i][0]}, {sorted_for_print[i][1]}), size: {sorted_for_print[i][2]}')

