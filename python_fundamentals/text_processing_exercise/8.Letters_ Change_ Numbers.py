data = [x.strip() for x in input().split()]

final_result = 0

for el in data:
    before = el[0]
    before_position = ord(before.lower()) - 96
    after = el[-1]
    after_position = ord(after.lower()) - 96
    number = int(''.join([x for x in el if x.isdigit()]))
    if before.isupper():
        result = number / before_position
    else:
        result = number * before_position
    if after.isupper():
        result -= after_position
    else:
        result += after_position
    final_result += result

print(f"{final_result:.2f}")