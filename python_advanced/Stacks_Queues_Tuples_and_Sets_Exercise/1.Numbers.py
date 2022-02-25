def numbers(seq):
    result = {int(x) for x in seq if x.isdigit()}
    return result


first = {int(x) for x in input().split()}
second = {int(x) for x in input().split()}

n = int(input())

for _ in range(n):
    command = input()
    if command == "Check Subset":
        print(True if first.issubset(second) or second.issubset(first) else False)
    elif "Add First" in command:
        command = command.split()
        nums = numbers(command)
        [first.add(x) for x in nums]
    elif "Add Second" in command:
        command = command.split()
        nums = numbers(command)
        [second.add(x) for x in nums]
    elif "Remove First" in command:
        command = command.split()
        nums = numbers(command)
        [first.remove(x) for x in nums if x in first]
    elif "Remove Second" in command:
        command = command.split()
        nums = numbers(command)
        [second.remove(x) for x in nums if x in second]

first_as_list = sorted([x for x in first])
second_as_list = sorted([x for x in second])

print(*first_as_list, sep=", ")
print(*second_as_list, sep=", ")