import sys

input = sys.stdin.readline

TC = int(input().strip())
for _ in range(TC):
    N = int(input().strip())
    candidates = []
    for _ in range(N):
        candidates.append(list(map(int, input().split())))

    candidates.sort()

    cnt = 1
    max_i = candidates[0][1]
    for d, i in candidates[1:]:
        if i < max_i:
            cnt += 1
        max_i = min(max_i, i)
    print(cnt)
