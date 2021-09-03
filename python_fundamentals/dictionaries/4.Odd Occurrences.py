word_list = input().split()

dictionary = {}

for word in word_list:
    key_lower = word.lower()
    if key_lower in dictionary:
        dictionary[key_lower] += 1
    else:
        dictionary[key_lower] = 1

for key, value in dictionary.items():
    if not value % 2 == 0:
        print(key, end=" ")