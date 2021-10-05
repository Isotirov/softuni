# int_string = [int(x) for x in input().split()]
#
# reverse_int_string = []
#
# for _ in range(len(int_string)):
#     reverse_int_string.append(int_string.pop())
#
# print(*reverse_int_string)


integers = [int(el) for el in input().split()]

rev_ints = []

while integers:
    rev_ints.append(integers.pop())

print(*rev_ints)