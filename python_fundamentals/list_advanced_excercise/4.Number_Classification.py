number_list = input().split(", ")

positive_list = [x for x in number_list if int(x) >= 0]
negative_list = [x for x in number_list if int(x) < 0]
even_list = [x for x in number_list if int(x) % 2 == 0]
odd_list = [x for x in number_list if not int(x) % 2 == 0]

print(f"Positive: {', '.join(positive_list)}")
print(f"Negative: {', '.join(negative_list)}")
print(f"Even: {', '.join(even_list)}")
print(f"Odd: {', '.join(odd_list)}")