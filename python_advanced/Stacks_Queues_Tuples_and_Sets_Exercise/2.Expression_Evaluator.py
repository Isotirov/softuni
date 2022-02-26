from collections import deque

string = input().split()

numbers = deque()
signs = ["+", "-", "*", "/"]

for char in string:
    if char in signs:
        if char == "/":
            to_process = "//".join(numbers)
        else:
            to_process = char.join(numbers)
        numbers = deque()
        numbers.append(str(eval(to_process)))
    else:
        numbers.append(char)

print(*numbers)