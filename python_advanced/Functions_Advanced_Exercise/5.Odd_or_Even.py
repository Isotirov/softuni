# command = input()
#
# numbers = [int(x) for x in input().split()]
#
# if command == "Even":
#     result = sum(filter(lambda x: x % 2 == 0, numbers)) * len(numbers)
# else:
#     result = sum(filter(lambda x: not x % 2 == 0, numbers)) * len(numbers)
#
# print(result)


def action(nums, com):
    if com == "Even":
        n = [x for x in nums if x % 2 == 0]
    else:
        n = [x for x in nums if not x % 2 == 0]
    return sum(n) * len(nums)


command = input()
numbers = [int(x) for x in input().split()]

print(action(numbers, command))
