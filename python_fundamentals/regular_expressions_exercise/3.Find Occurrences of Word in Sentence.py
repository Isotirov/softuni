import re

text = input().lower()

pattern = rf"\b{input().lower()}\b"

print(len(re.findall(pattern, text)))