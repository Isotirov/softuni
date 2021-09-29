def sum_ascii(word):
    result = 0
    for char in word:
        result += ord(char)
    return result


odd = set()
even = set()

n = int(input())

for row in range(1, n+1):
    current_result = int(sum_ascii(input()) / row)
    even.add(current_result) if current_result % 2 == 0 else odd.add(current_result)

sum_odd = sum(odd)
sum_even = sum(even)

if sum_even == odd:
    result = odd.union(even)
elif sum_even < sum_odd:
    result = odd.difference(even)
else:
    result = odd.symmetric_difference(even)
print(*result, sep=", ")