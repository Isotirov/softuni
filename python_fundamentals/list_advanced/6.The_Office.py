employees_happiness = [int(x) for x in input().split()]
factor = int(input())
happy_list = list(map(lambda x: x * factor, employees_happiness))

average_happiness = (sum(happy_list) / len(happy_list))

happy_people = [x for x in happy_list if x >= average_happiness]

if len(happy_people) >= len(happy_list) / 2:
    print(f"Score: {len(happy_people)}/{len(happy_list)}. Employees are happy!")
else:
    print(f"Score: {len(happy_people)}/{len(happy_list)}. Employees are not happy!")