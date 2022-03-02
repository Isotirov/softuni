from collections import deque


def honey_calculate(bee, nect, process):
    if process == "+":
        return abs(bee + nect)
    elif process == "-":
        return abs(bee - nect)
    elif process == "/":
        if nect > 0:
            return abs(bee / nect)
        return 0
    elif process == "*":
        return abs(bee * nect)


working_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
honey_making_process = deque(input().split())

collected_honey = 0

while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()
    if current_nectar >= current_bee:
        collected_honey += honey_calculate(current_bee, current_nectar, honey_making_process.popleft())
    else:
        working_bees.appendleft(current_bee)

print(f"Total honey made: {collected_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")