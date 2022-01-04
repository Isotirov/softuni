def operate(operator, *args):
    if operator == "/":
        result = args[0]*args[0]
        for num in args:
            result /= num
    elif operator == "-":
        result = args[0]+args[0]
        for num in args:
            result -= num
    elif operator == "+":
        result = 0
        for num in args:
            result += num
    elif operator == "*":
        result = 1
        for num in args:
            result *= num
    return result
