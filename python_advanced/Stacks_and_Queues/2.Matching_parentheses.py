# string = input()
#
# s = []
#
# for i in range(len(string)):
#     if string[i] == "(":
#         s.append(i)
#     elif string[i] == ")":
#         j = s.pop()
#         print(string[j:i+1])


expression = input()

parentheses = []

for i in range(len(expression)):
    if expression[i] == "(":
        parentheses.append(i)
    elif expression[i] == ")":
        start_expression = parentheses.pop()
        end_expression = i
        print(expression[start_expression:end_expression+1])