# REF https://www.acmicpc.net/problem/18258
# Sliver 4

# 정수를 저장하는 큐를 구현한 후, 입력으로 주어지는 명령을 처리하라.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 입력
# 명령의 수 N 1 <= N <= 2,000,000

import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
dq = deque()

for _ in range(n):
    cmd = input().strip()
    if len(cmd) > 5:
        cmd, val = cmd.split()
        dq.append(int(val))
    elif cmd == "pop":
        print("-1" if len(dq) == 0 else str(dq.popleft()))
    elif cmd == "size":
        print(str(len(dq)))
    elif cmd == "empty":
        print("1" if len(dq) == 0 else "0")
    elif cmd == "front":
        print("-1" if len(dq) == 0 else str(dq[0]))
    elif cmd == "back":
        print("-1" if len(dq) == 0 else str(dq[-1]))


def solution(n, cmds, ans):
    dq = deque()
    for i in range(n):
        sol = None
        if len(cmds[i]) > 5:
            cmd, val = cmds[i].split()
            dq.append(int(val))
        elif cmds[i] == "pop":
            sol = "-1" if len(dq) == 0 else str(dq.popleft())
        elif cmds[i] == "size":
            sol = str(len(dq))
        elif cmds[i] == "empty":
            sol = "1" if len(dq) == 0 else "0"
        elif cmds[i] == "front":
            sol = "-1" if len(dq) == 0 else str(dq[0])
        elif cmds[i] == "back":
            sol = "-1" if len(dq) == 0 else str(dq[-1])

        print(sol == ans[i])


"""
solution(
    15,
    [
        "push 1",
        "push 2",
        "front",
        "back",
        "size",
        "empty",
        "pop",
        "pop",
        "pop",
        "size",
        "empty",
        "pop",
        "push 3",
        "empty",
        "front",
    ],
    [
        None,
        None,
        "1",
        "2",
        "2",
        "0",
        "1",
        "2",
        "-1",
        "0",
        "1",
        "-1",
        None,
        "0",
        "3",
    ],
)
"""
