def calculations(operation, int_1, int_2):
    if operation == "multiply":
        result = int_1 * int_2
        return result
    elif operation == "divide":
        result = int(int_1 / int_2)
        return result
    elif operation == "add":
        result = int_1 + int_2
        return result
    elif operation == "subtract":
        result = int_1 - int_2
        return result


operator = input()
num_1 = int(input())
num_2 = int(input())
print(calculations(operator, num_1, num_2))