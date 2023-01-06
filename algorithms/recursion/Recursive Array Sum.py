arr = [int(x) for x in input().split()]


def calc_sum(idx, array):
    if idx >= len(array) - 1:
        return array[idx]
    return array[idx] + calc_sum(idx + 1, array)


print(calc_sum(0, arr))
