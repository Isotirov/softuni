n = int(input())

array = [None] * n


def loop(idx, arr):
    if idx >= len(arr):
        print(*arr, sep=' ')
        return
    for i in range(1, len(arr) + 1):
        arr[idx] = i
        loop(idx + 1, arr)


loop(0, array)
