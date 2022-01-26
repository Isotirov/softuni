# def even(nums):
#     return nums % 2 == 0
#
#
# def odd(nums):
#     return not even(nums)
#
#
# def even_odd(*args):
#     if args[-1] == "even":
#         return list(filter(even, args[:-1]))
#     return list(filter(odd, args[:-1]))
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))


def even_odd(*args):
    command = args[-1]
    print(command)
    return [int(x) for x in args[:-1] if x % 2 == 0] if command == "even" else [int(x) for x in args[:-1] if not x % 2 == 0]
