# array = [int(x) for x in input().split()]
#
# searched = int(input())
#
#
# def binary_search(arr, search):
#     left_idx = 0
#     right_idx = len(arr) - 1
#
#     while left_idx <= right_idx:
#
#         middle = (left_idx + right_idx) // 2
#
#         if search == arr[middle]:
#             return middle
#         if search < arr[middle]:
#             right_idx = middle
#         else:
#             left_idx = middle
#
#     return -1
#
#
# print(binary_search(array, searched))
