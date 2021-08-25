explosion = list(input())

power = 0
i = 0

while i < len(explosion):
    if explosion[i] == ">":
        if explosion[i+1].isdigit():
            power += int(explosion[i+1])
    for _ in range(power):
        if not explosion[i+1] == ">":
            explosion.pop(i+1)
            power -= 1
    i += 1
print(''.join(explosion))