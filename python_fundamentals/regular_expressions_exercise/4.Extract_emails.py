import re

text = input()

pattern = r"(^|(?<=\s))[a-z0-9]+[-._]?[a-z0-9]+@[a-z]+([.-][a-z]+)+\b"

emails = re.finditer(pattern, text)

print('\n'.join([mail.group() for mail in emails]))