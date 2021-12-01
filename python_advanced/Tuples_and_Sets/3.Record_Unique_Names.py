# def input_to_list(num):
#     lines = []
#     for _ in range(num):
#         lines.append(input())
#     return lines
#
#
# n = int(input())
# names = set(input_to_list(n))
#
# [print(x) for x in names]


n = int(input())

some_set = {input() for x in range(n)}

[print(x) for x in some_set]