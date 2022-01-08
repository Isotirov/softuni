def expressions(nums, result=0, current_exp=""):
    if not nums:
        print(f"{current_exp}={result}")
        return
    expressions(nums[1:], result+nums[0], f"{current_exp}+{nums[0]}")
    expressions(nums[1:], result-nums[0], f"{current_exp}-{nums[0]}")


numbers = [int(x) for x in input().split(", ")]
expressions(numbers)