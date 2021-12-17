n = int(input())

odd_set = set()
even_set = set()

for row in range(1, n+1):
    ascii_sum = 0
    name = input()
    for char in name:
        ascii_sum += ord(char)
    result = int(ascii_sum / row)
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

sum_odd_set = sum(odd_set)
sum_even_set = sum(even_set)

if sum_odd_set == sum_even_set:
    print(', '.join(str(x) for x in odd_set.union(even_set)))
elif sum_odd_set > sum_even_set:
    print(', '.join(str(x) for x in odd_set.difference(even_set)))
else:
    print(', '.join(str(x) for x in odd_set.symmetric_difference(even_set)))