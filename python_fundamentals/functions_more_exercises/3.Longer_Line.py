import math


def longer_line(p1, y1, p2, y2, p3, y3, p4, y4):
    first_line = (point_1_x - point_2_x) ** 2 + (point_1_y - point_2_y) ** 2
    second_line = (point_3_x - point_3_x) ** 2 + (point_4_y - point_4_y) ** 2
    if first_line <= second_line:
        point_1 = (point_1_x ** 2 + point_1_y ** 2)
        point_2 = (point_2_x ** 2 + point_2_y ** 2)
        if point_1 <= point_2:
            return f"({math.floor(point_1_x)}, {math.floor(point_1_y)})({math.floor(point_2_x)}, {math.floor(point_2_y)})"
        return f"({math.floor(point_2_x)}, {math.floor(point_2_y)})({math.floor(point_1_x)}, {math.floor(point_1_y)})"
    point_3 = point_3_x ** 2 + point_3_y ** 2
    point_4 = point_4_x ** 2 + point_4_y ** 2
    if point_3 <= point_4:
        return f"({math.floor(point_3_x)}, {math.floor(point_3_y)})({math.floor(point_4_x)}, {math.floor(point_4_y)})"
    return f"({math.floor(point_4_x)}, {math.floor(point_4_y)})({math.floor(point_3_x)}, {math.floor(point_3_y)})"


point_1_x = float(input())
point_1_y = float(input())
point_2_x = float(input())
point_2_y = float(input())
point_3_x = float(input())
point_3_y = float(input())
point_4_x = float(input())
point_4_y = float(input())
print(longer_line(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y, point_4_x, point_4_y))