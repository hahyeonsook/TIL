import sys, bisect

input = sys.stdin.readline
N, M = map(int, input().split())
seq = []

for _ in range(N):
    seq.append(int(input().strip()))

seq = sorted(seq)

val = 0
answer = 2000001
left, right = 0, 0
while left < N and right < N:
    val = seq[right] - seq[left]
    if val < M:
        right += 1
    else:
        left += 1
        answer = answer if abs(M - answer) < abs(M - val) else val

    if val == M:
        break

print(answer)
