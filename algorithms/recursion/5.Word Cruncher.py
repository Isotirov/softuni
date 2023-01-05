words = [x for x in input().split(', ')]
searched = input()

words_by_idx = {}
words_by_count = {}

for word in words:
    if word in words_by_count:
        words_by_count[word] += 1
        continue
    words_by_count[word] = 1

    idx = 0
    try:
        while True:
            idx = searched.index(word, idx)
            if idx not in words_by_idx:
                words_by_idx[idx] = []
            words_by_idx[idx].append(word)
            idx += len(word)
    except ValueError:
        pass


def crunch(idx, result):
    if idx >= len(searched):
        print(*result, sep=' ')
        return

    if idx not in words_by_idx:
        return
    for word in words_by_idx[idx]:
        if words_by_count[word] > 0:
            words_by_count[word] -= 1
            result.append(word)
            crunch(idx + len(word), result)
            words_by_count[word] += 1
            result.remove(word)


crunch(0, [])

