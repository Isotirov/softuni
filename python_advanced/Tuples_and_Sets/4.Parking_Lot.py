# n = int(input())
#
# cars = set()
#
# for _ in range(n):
#     direction, license_plate = input().split(", ")
#     if direction == "IN":
#         cars.add(license_plate)
#     else:
#         cars.remove(license_plate)
#
# if cars:
#     [print(x) for x in cars]
# else:
#     print("Parking Lot is Empty")


n = int(input())

lot = set()

for _ in range(n):
    direction, license = input().split(", ")
    if direction == "IN":
        lot.add(license)
    else:
        lot.remove(license)

if not lot:
    print("Parking Lot is Empty")
else:
    [print(x) for x in lot]