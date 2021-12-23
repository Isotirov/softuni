def rounding(lst):
    rounded_list = [round(x) for x in lst]
    return rounded_list


numbers = [float(x) for x in input().split()]

print(rounding(numbers))