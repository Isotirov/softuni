# array = [int(x) for x in input().split()]
#
#
# def selection_sort(arr):
#     for idx in range(len(arr)):
#         for i in range(idx, len(arr)):
#             if arr[idx] > arr[i]:
#                 arr[idx], arr[i] = arr[i], arr[idx]
#
#
# selection_sort(array)
# print(*array, sep=' ')


# numbers = [int(x) for x in input().split()]
#
#
# def selection_sort(nums):
#     for i in range(len(nums)):
#         idx = i
#         while idx < len(nums):
#             if nums[i] > nums[idx]:
#                 nums[i], nums[idx] = nums[idx], nums[i]
#             idx += 1
#
#
# selection_sort(numbers)
# print(*numbers, sep=' ')


nums = [int(x) for x in input().split()]


def selection(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


selection(nums)
print(nums)
