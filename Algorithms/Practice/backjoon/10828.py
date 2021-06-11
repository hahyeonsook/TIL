# REF https://www.acmicpc.net/problem/10828
# Silver 4

# 스택을 구현한 후 입력으로 주어지는 명령을 처리해라
# PUSH X, X를 스택에 넣는다.
# POP: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 정수가 없을 경우 -1을 출력한다.
# SIZE: 스택에 들어있는 정수의 개수를 출력한다.
# EMPTY: 스택이 비면 1, 아니면 0을 출력한다.
# TOP: 스택의 가장 위에 있는 수를 출력한다. 비었을 경우 -1을 출력한다.

# 입력
# 1 <= N <= 10,000

# sys를 쓰는 이유
# https://www.acmicpc.net/problem/15552
import sys

input = sys.stdin.readline

n = int(input().strip())
_list = []

for _ in range(n):
    cmd = input().strip()

    if cmd > 5:
        cmd, val = cmd.split()
        _list.append(int(val))
    elif cmd == "pop":
        print("-1" if len(_list) == 0 else str(_list.pop()))
    elif cmd == "size":
        print(str(len(_list)))
    elif cmd == "empty":
        print("1" if len(_list) == 0 else "0")
    elif cmd == "top":
        print("-1" if len(_list) == 0 else str(_list[-1]))


def solution(n, cmds, ans):
    _list = []

    for i in range(n):
        sol = None
        if "push" in cmds[i]:
            cmds[i], val = cmds[i].split()
            _list.append(int(val))
        else:
            if cmds[i] == "pop":
                sol = -1 if len(_list) == 0 else _list.pop()
            elif cmds[i] == "size":
                sol = len(_list)
            elif cmds[i] == "empty":
                sol = 1 if len(_list) == 0 else 0
            elif cmds[i] == "top":
                sol = -1 if len(_list) == 0 else _list[-1]

        print(sol == ans[i])


"""
print("예제 1")
solution(
    14,
    [
        "push 1",
        "push 2",
        "top",
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
        "top",
    ],
    [
        None,
        None,
        2,
        2,
        0,
        2,
        1,
        -1,
        0,
        1,
        -1,
        None,
        0,
        3,
    ],
)

print("예제 2")
solution(
    7,
    [
        "pop",
        "top",
        "push 123",
        "top",
        "pop",
        "top",
        "pop",
    ],
    [
        -1,
        -1,
        None,
        123,
        123,
        -1,
        -1,
    ],
)
"""
