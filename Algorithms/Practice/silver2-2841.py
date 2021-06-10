# 손가락이 수억개인 외계인이 기타를 친다.
# 기타는 6개의 줄이 있고, 각 줄은 P개의 프렛으로 나눠져있다.
# 프렛을 누른 상태로 줄을 튕기면 음을 연주할 수 있는데, 어떤 줄의 프렛을 여러 개 누르고 잇다면 가장 높은 음이 들린다.
# 손가락으로 프렛을 누르거나 떼는 것을 한 번 움직였다고 할 때, 횟수를 최소화하는 방법을 구하는 프로그램을 작성하라.

# 시간초과
# 아이디어는 맞았는데, 시간초과함.

N, P = map(int, input().split())

notes = [[] for _ in range(6)]
cnt = 0
# O(N) => 500,000
for _ in range(N):
    line, fret = map(lambda x: int(x) - 1, input().split())

    # O(N-1) => 300,000
    while notes[line] and notes[line][-1] > fret:
        notes[line].pop()
        cnt += 1
    if len(notes[line]) == 0 or notes[line][-1] < fret:
        notes[line].append(fret)
        cnt += 1

print(cnt)

# 파이썬은 초당 20,000,000 가능
# 150,000,000,000

# 통과사례
n, p = map(int, input().split())
ch = [[] for _ in range(8)]
cnt = 0
for _ in range(n):
    high, frat = map(int, input().split())
    while ch[high] and ch[high][-1] > frat:
        ch[high].pop()
        cnt += 1
    if ch[high] and ch[high][-1] == frat:
        ch[high].pop()
        cnt -= 1
    ch[high].append(frat)
    cnt += 1

print(cnt)
