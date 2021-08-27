integer_list = [int(x) for x in input().split(", ")]

start = 0
group = 10

while len(integer_list) > 0:
    filtered_list = [x for x in integer_list if start < x <= group]
    for i in filtered_list:
        integer_list.remove(i)
    print(f"Group of {group}'s: {filtered_list}")
    start += 10
    group += 10