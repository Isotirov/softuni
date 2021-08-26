int_string = [int(x) for x in input().split(", ")]

evens_list = []

for i in range(len(int_string)):
    if int_string[i] % 2 == 0:
        evens_list.append(i)

print(evens_list)