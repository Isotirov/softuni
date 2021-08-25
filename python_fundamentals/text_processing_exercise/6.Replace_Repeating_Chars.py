string = input()

index = 0
to_replace = ""

while index < len(string)-1:

    if string[index] == string[index + 1]:
        to_replace = string[index]+string[index+1]
        string = string.replace(to_replace, string[index])
    else:
        index += 1

print(string)