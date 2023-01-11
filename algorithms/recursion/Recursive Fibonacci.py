n = int(input())


def fibonacci(num):
    if num == 0:
        return 1
    if num == 1:
        return 1

    return fibonacci(num-1) + fibonacci(num-2)


print(fibonacci(n))


# n = int(input())
#
#
# def fib(n):
#     if n <= 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(n))