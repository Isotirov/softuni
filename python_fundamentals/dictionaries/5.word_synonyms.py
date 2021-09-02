n = int(input())

synonym_dict = {}

for _ in range(n):
    word = input()
    synonym = input()
    if word not in synonym_dict:
        synonym_dict[word] = []
    synonym_dict[word].append(synonym)

for key in synonym_dict:
    print(f"{key} - {', '.join(synonym_dict[key])}")