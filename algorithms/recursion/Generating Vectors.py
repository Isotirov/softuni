n = int(input())

vector = [0] * n


def vectors(idx, arr):
    if idx >= len(arr):
        print(*arr, sep='')
        return
    for i in range(2):
        arr[idx] = i
        vectors(idx+1, arr)


vectors(0, vector)
