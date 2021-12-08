# n = int(input())
#
# usernames = set()
#
# for _ in range(n):
#     user = input()
#     usernames.add(user)
#
# [print(x) for x in usernames]


n = int(input())

unique_usernames = set()

[unique_usernames.add(input()) for x in range(n)]

[print(x) for x in unique_usernames]