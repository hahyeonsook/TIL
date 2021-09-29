import sys

input = sys.stdin.readline

N = int(input().strip())
people = sorted(list(map(int, input().split())))
"""
# 68ms
ans = people[0]
for idx in range(1, N):
    people[idx] = people[idx - 1] + people[idx]
    ans += people[idx]
print(ans)

# 68ms
ans = people[0]
prev = people[0]
for idx in range(1, N):
    people[idx] = prev + people[idx]
    prev = people[idx]
    ans += prev

print(ans)

# 64ms
ans, tmp = 0, 0
for p in people:
    tmp += p
    ans += tmp
print(ans)
"""
sum_t, a = 0, N

for i in range(N):
    # 1 + (1 + 2) + (1 + 2 + 3) + (1 + 2 + 3 + 3) + (1 + 2 + 3 + 3 + 4)
    # 1*5 + 2*4 + 3*3 + 3*2 + 4*1
    tt = people[i] * a
    sum_t += tt
    a -= 1

print(sum_t)
