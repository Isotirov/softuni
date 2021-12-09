text = input()

char_count = {}

for char in text:
    if char not in char_count:
        char_count[char] = 0
    char_count[char] += 1

char_count = sorted(char_count.items(), key=lambda x: ord(x[0]))

for key, value in char_count:
    print(f"{key}: {value} time/s")