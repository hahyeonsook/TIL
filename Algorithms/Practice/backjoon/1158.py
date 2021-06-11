# REF https://www.acmicpc.net/problem/1158
# Silver 5

# N 명의 사람이 원을 이루며 앉아있다.
# N 명이 모두 제거될 때까지 K 번째 사람을 제거하는 것을 반복한다.
# 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라 한다. EX) (7, 3)-요세푸스 순열: <3, 6, 2, 7, 5, 1>

# 입력
# 1 <= K <= N <= 5,000

# 출력
# < 3, 6, 2, 7, 5, 1, 4>

# 반례 (1, 1)

from collections import deque
import collections

# 멍청인가..? k를 안넣고 2로 넣어서 돌림
# queue는 멀티스레딩 용도여서 비효율적이다.
def solution(n, k, collect):
    dq = deque([(i + 1) for i in range(n)])
    sol = "<"
    removed = 0

    # O(N)
    for _ in range(n):
        # O(2)
        dq.rotate(-(k - 1))
        removed = dq.popleft()

        if len(dq) != 0:
            sol += f"{removed}, "
        else:
            sol += f"{removed}>"

    if sol == collect:
        print("맞았습니다!")
    else:
        print(f"틀렸습니다! {sol}")


solution(3, 2, "<2, 3, 1>")

"""
반례 (1, 1)
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dq = deque([i + 1 for i in range(n)])
sol = ""

while len(dq) != 0:
    dq.rotate(-2)
    removed = dq.popleft()

    if len(sol) == 0:
        sol += f"<{removed}, "
    elif len(dq) == 0:
        sol += f"{removed}>"
    else:
        sol += f"{removed}, "

print(sol)
"""

"""
from collections import deque

n, k = map(int, input().split())

dq = deque([i + 1 for i in range(n)])
sol = "<"

while len(dq) != 0:
    dq.rotate(-k)
    removed = dq.popleft()

    if len(dq) != 0:
        sol += f"{removed}, "
    else:
        sol += f"{removed}>"

print(sol)
"""
