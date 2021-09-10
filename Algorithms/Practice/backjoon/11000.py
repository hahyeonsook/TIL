import sys, heapq

input = sys.stdin.readline
N = int(input().strip())

rooms = []
classes = []
for index in range(N):
    s, e = map(int, input().split())
    heapq.heappush(classes, (s, e))

upped = False
while classes:
    s, e = heapq.heappop(classes)
    if not rooms:
        rooms.append([s, e])
        continue

    for idx in range(len(rooms)):
        if rooms[idx][1] <= s:
            rooms[idx][1] = e
            upped = True
            break
    if upped:
        rooms.append([s, e])
        upped = False

print(len(rooms))
