new_string = [x for x in input() if x not in ('a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I')]
print("".join(new_string))