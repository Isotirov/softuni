# def input_to_list(num):
#     lines = set()
#     for _ in range(num):
#         lines.add(input())
#     return lines
#
#
# n = int(input())
# guest_list = input_to_list(n)
#
# coming_guests = set()
#
# while True:
#     guest = input()
#     if guest == "END":
#         break
#     else:
#         coming_guests.add(guest)
#
# did_not_come = guest_list - coming_guests
#
# print(len(did_not_come))
#
# did_not_come = sorted(did_not_come)
#
# [print(x) for x in did_not_come if x[0].isdigit()]
# [print(x) for x in did_not_come if not x[0].isdigit()]


n = int(input())

all_guests = {input() for x in range(n)}
coming = set()

while True:
    command = input()
    if command == "END":
        break
    coming.add(command)

did_not_come = all_guests - coming

print(len(did_not_come))
[print(x) for x in sorted(did_not_come) if x.isdigit()]
[print(x) for x in sorted(did_not_come) if not x.isdigit()]