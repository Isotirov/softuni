def multiply(str_1, str_2):
    result = 0
    for i in range(0, len(str_1)):
        result += ord(str_1[i]) * ord(str_2[i])
    return result


word_1, word_2 = input().split()

if len(word_1) > len(word_2):
    total_sum = multiply(word_2, word_1)
    for x in range(len(word_2), len(word_1)):
        total_sum += ord(word_1[x])
elif len(word_1) < len(word_2):
    total_sum = multiply(word_1, word_2)
    for x in range(len(word_1), len(word_2)):
        total_sum += ord(word_2[x])
else:
    total_sum = multiply(word_1, word_2)

print(total_sum)