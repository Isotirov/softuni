# def input_to_lines(num):
#     lines = set()
#     for _ in range(num):
#         line = input()
#         if " " in line:
#             line = line.split()
#             for el in line:
#                 lines.add(el)
#         else:
#             lines.add(line)
#     return lines
#
#
# n = int(input())
# elements = input_to_lines(n)
#
#
# [print(el) for el in elements]


n = int(input())

p_table = set()

for _ in range(n):
    elements = input().split()
    [p_table.add(x) for x in elements]

[print(el) for el in p_table]