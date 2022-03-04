from collections import deque

string = deque(input().split())

main_colors = {"red", "yellow", "blue"}
sub_colors = {"orange", "purple", "green"}

secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

crafted_colors = []

while string:
    start = string.popleft()
    if string:
        end = string.pop()
    else:
        end = ""
    color = start + end
    if color in main_colors or color in sub_colors:
        crafted_colors.append(color)
        continue
    color = end + start
    if color in main_colors or color in sub_colors:
        crafted_colors.append(color)
        continue
    return_string_left = start[:-1]
    return_string_right = end[:-1]
    if return_string_left:
        string.insert(len(string) // 2, return_string_left)
    if return_string_right:
        string.insert(len(string) // 2, return_string_right)

# print(crafted_colors)
for color in crafted_colors:
    if color in main_colors:
        continue

    if color in secondary_colors:
        searched_colors = secondary_colors[color]
        for s in searched_colors:
            if s not in crafted_colors:
                crafted_colors.remove(color)
                break
    else:
        crafted_colors.remove(color)

print(crafted_colors)