def combinations(string, i=0):
    if i >= len(string):
        print("".join(string))
        return

    combinations(string, i+1)
    for j in range(i+1, len(string)):
        string[i], string[j] = string[j], string[i]
        combinations(string, i + 1)
        string[i], string[j] = string[j], string[i]


string_console = list(input())
combinations(string_console)