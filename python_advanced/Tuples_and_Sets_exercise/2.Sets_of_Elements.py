# def input_to_line(num):
#     lines = set()
#     for _ in range(num):
#         lines.add(input())
#     return lines
#
#
# n, m = input().split()
# n = int(n)
# m = int(m)
#
# n_set = input_to_line(n)
# m_set = input_to_line(m)
#
# repeat_elements = n_set.intersection(m_set)
#
# [print(x) for x in repeat_elements]


def add_set(x):
    some_set = set()
    for _ in range(x):
        some_set.add(input())
    return some_set


n, m = input().split()
n = int(n)
m = int(m)

first_set = add_set(n)
second_set = add_set(m)

result = first_set.intersection(second_set)

[print(x) for x in result]