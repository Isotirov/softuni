def absolute_values(lst):
    absolute_list = list(map(lambda x: abs(x), lst))
    # for i in lst:
    #     absolute_list.append(abs(i))
    return absolute_list


numbers = [float(x) for x in input().split()]

print(absolute_values(numbers))