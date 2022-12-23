array = list(input().split())


def reverse_arr(idx, arr):
    last_idx = len(arr) - 1 - idx
    if int(len(arr) / 2) == idx:
        return
    arr[idx], arr[last_idx] = arr[last_idx], arr[idx]
    reverse_arr(idx + 1, arr)


reverse_arr(0, array)
print(' '.join(array))
