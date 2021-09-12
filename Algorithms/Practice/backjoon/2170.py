import sys

input = sys.stdin.readline
N = int(input().strip())

lines = []
for _ in range(N):
    lines.append(list(map(int, input().split())))

length = 0
lines.sort()
x, y = lines[0]
for p1, p2 in lines:
    if p1 > y:
        length += abs(y - x)
        x, y = p1, p2
        continue
    y = max(y, p2)

length += abs(y - x)
print(length)
