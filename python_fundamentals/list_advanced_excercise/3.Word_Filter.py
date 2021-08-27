word_filter = [x for x in input().split() if len(x) % 2 == 0]
for word in word_filter:
    print(word)