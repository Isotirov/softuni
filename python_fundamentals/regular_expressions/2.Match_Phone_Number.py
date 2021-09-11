import re

data = input()

pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"

matches = [x.group() for x in re.finditer(pattern, data)]

print(', '.join(matches))