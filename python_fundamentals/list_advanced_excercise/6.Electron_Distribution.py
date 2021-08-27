number_of_electrons = int(input())

shells_list = []

start_shell = 1

while number_of_electrons > 0:
    shell_capacity = 2 * (start_shell ** 2)
    if number_of_electrons - shell_capacity >= 0:
        number_of_electrons -= shell_capacity
        shells_list.append(shell_capacity)
        start_shell += 1
    else:
        shells_list.append(number_of_electrons)
        number_of_electrons -= shell_capacity
print(shells_list)