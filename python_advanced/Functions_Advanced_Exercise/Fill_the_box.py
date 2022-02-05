from collections import deque


def fill_the_box(*args):
    nums = deque()
    for a in args:
        if a == "Finish":
            break
        nums.append(int(a))
    size = nums.popleft() * nums.popleft() * nums.popleft()
    rest = sum(nums)
    if rest < size:
        return f"There is free space in the box. You could put {size - rest} more cubes."
    return f"No more free space! You have {rest - size} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))