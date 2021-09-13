import re

data = input()

pattern = r"\b(?P<underscore>_)(?P<var>[A-Za-z0-9]+)\b"

matches = re.finditer(pattern, data)
var_s = [x.group("var") for x in matches]

print(*var_s, sep=",")