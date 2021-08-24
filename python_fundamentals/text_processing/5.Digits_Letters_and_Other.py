text = input()

print(''.join(list(filter(lambda x: x.isdigit(), text))))
print(''.join(list(filter(lambda x: x.isalpha(), text))))
print(''.join(list(filter(lambda x: not x.isdigit() and not x.isalpha(), text))))