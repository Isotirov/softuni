from collections import deque

kids = deque((input().split()))

toss = int(input())

while kids:
    for _ in range(toss-1):
        kids.append(kids.popleft())
    if len(kids) == 1:
        print(f"Last is {kids.popleft()}")
        break
    else:
        print(f"Removed {kids.popleft()}")
