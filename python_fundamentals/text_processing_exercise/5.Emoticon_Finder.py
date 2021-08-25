text = input()

emoticons = [f"{text[x]}{text[x+1]}" for x in range(len(text)) if text[x] == ":"]

print('\n'.join(emoticons))