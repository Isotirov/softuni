rooms = int(input())

total_chairs = 0
total_visitors = 0

for room in range(1, rooms+1):
    room_state = input().split()
    chairs = len(room_state[0])
    visitors = int(room_state[1])
    total_chairs += chairs
    total_visitors += visitors
    if visitors > chairs:
        needed_chairs = visitors - chairs
        print(f"{needed_chairs} more chairs needed in room {room}")
if total_chairs >= total_visitors:
    free_chairs = total_chairs - total_visitors
    print(f"Game On, {free_chairs} free chairs left")