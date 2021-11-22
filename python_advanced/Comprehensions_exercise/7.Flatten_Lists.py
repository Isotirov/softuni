# matrix = [[j for j in x.split() if not j == " "] for x in input().split("|")[::-1]]

# print(' '.join([num for sublist in [[j for j in x.split() if not j == " "] for x in input().split("|")[::-1]]
#                 for num in sublist]))


print(' '.join(el for row in [[j for j in x.split()] for x in input().split("|")][::-1] for el in row))