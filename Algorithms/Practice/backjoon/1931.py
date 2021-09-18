import sys

input = sys.stdin.readline
N = int(input().strip())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))

meetings = sorted(meetings)

cnt = 1
schedule = meetings[0][1]
for start, end in meetings[1:]:
    if schedule > start and schedule < end:
        continue

    if schedule <= start:
        cnt += 1
    schedule = end

print(cnt)
