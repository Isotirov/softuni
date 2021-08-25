text = [x for x in input()]

new_text = [chr(ord(x)+3) for x in text]

print(''.join(new_text))