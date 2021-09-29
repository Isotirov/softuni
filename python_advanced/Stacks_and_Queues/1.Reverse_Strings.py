# text = list(input())
#
# for _ in range(len(text)):
#     print(text.pop(), end="")


text = list(input())

reversed_text = []
for _ in range(len(text)):
    reversed_text.append(text.pop())

print(''.join(reversed_text))