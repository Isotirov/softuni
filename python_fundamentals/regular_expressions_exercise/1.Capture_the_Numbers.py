import re

pattern = r"\d+"
data = input()

while data:

    matches = re.finditer(pattern, data)

    for match in matches:
        if match:
            print(match.group(), end=" ")