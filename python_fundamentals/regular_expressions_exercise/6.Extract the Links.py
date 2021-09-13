import re

pattern = r"(www)\.([A-Za-z0-9]+(-[A-Za-z0-9]+)*)(\.[a-z]+)+"

data = input()
urls = []

while data:
    match = re.finditer(pattern, data)
    for i in match:
        if i:
            urls.append(i.group())
    data = input()

for url in urls:
    print(url)