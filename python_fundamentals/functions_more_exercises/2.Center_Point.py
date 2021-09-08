import math


def closest_point(value1, value2, value3, value4):
    result = (value1 ** 2 + value2 ** 2)
    result_1 = (value3 ** 2 + value4 ** 2)
    if result > result_1:
        return print(f"({math.floor(value3)}, {math.floor(value4)})")
    return print(f"({math.floor(value1)}, {math.floor(value2)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
closest_point(x1, y1, x2, y2)