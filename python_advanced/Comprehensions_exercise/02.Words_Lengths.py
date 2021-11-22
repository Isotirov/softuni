# word_lengths = {word: len(word) for word in input().split(", ")}

print(", ".join([f'{word} -> {length}' for word, length in {word: len(word) for word in input().split(", ")}.items()]))