version = [int(x) for x in input().split(".")]

version[-1] += 1
if version[-1] == 10:
    version[-1] = 0
    version[1] += 1
    if version[1] == 10:
        version[1] = 0
        version[0] += 1
print(*version, sep=".")