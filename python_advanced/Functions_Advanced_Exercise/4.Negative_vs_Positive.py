# numbers = [int(x) for x in input().split()]
#
# sum_positive = sum(filter(lambda x: x >= 0, numbers))
# sum_negative = sum(filter(lambda x: x < 0, numbers))
#
# print(sum_negative)
# print(sum_positive)
#
# if sum_positive > abs(sum_negative):
#     print("The positives are stronger than the negatives")
# else:
#     print("The negatives are stronger than the positives")


def pos_neg(nums):
    pos = [x for x in nums if x >= 0]
    neg = [x for x in nums if x < 0]
    return sum(pos), sum(neg)


numbers = [int(x) for x in input().split()]
positive, negative = pos_neg(numbers)

print(negative)
print(positive)
if positive > abs(negative):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")