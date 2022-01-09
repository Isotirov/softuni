numbers = [int(x) for x in input().split()]

even_nums = list(filter(lambda x: x % 2 == 0, numbers))

print(even_nums)