n = int(input())

longest_intersection = set()

for _ in range(n):
    first_set = set()
    second_set = set()
    range_1, range_2 = input().split("-")
    first_start = int(range_1.split(",")[0])
    first_end = int(range_1.split(",")[1])
    second_start = int(range_2.split(",")[0])
    second_end = int(range_2.split(",")[1])
    for x in range(first_start, first_end+1):
        first_set.add(x)
    for y in range(second_start, second_end+1):
        second_set.add(y)
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")