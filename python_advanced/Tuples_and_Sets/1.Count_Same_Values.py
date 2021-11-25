# n = [float(x) for x in input().split(" ")]
#
# score = {}
#
# for num in n:
#     if num not in score:
#         score[num] = 0
#     score[num] += 1
#
# [print(f"{x} - {y} times") for x, y in score.items()]


numbers = [float(x) for x in input().split()]

counter = {}

for n in numbers:
    if n not in counter:
        counter[n] = 0
    counter[n] += 1

for number, count in counter.items():
    print(f"{number:.1f} - {count} times")