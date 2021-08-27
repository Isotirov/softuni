first_sequence = input().split(", ")
second_sequence = input().split(", ")

new_sequence = []

for i in first_sequence:
    for ii in second_sequence:
        if i in ii and i not in new_sequence:
            new_sequence.append(i)
print(new_sequence)