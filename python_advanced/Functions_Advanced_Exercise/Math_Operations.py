def math_operations(*args, **kwargs):
    nums = [int(x) for x in args]
    count = 0
    for a in nums:
        count += 1
        if count == 5:
            count = 1
        if count == 1:
            kwargs["a"] += a
        elif count == 2:
            kwargs["s"] -= a
        elif count == 3:
            if a == 0:
                continue
            kwargs["d"] /= a
        elif count == 4:
            kwargs["m"] *= a
    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))