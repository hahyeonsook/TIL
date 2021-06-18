# REF https://www.acmicpc.net/problem/1874
# Sliver 3
# 2초 40,000,000 연산 안에 끝내야 함.

# 스택의 push 순서는 오름차순을 지킨다.
# 임의의 수열이 주어졌을 때, 스택을 이용해 그 수열을 만들 수 있는지 없는지 알아내라.
# 만들 수 있다면, push/pop 연산의 순서를 나타내라

# 입력
# 첫 줄, n, 1 <= n <= 100,000
# n개의 줄, x, 수열을 이루는 1 <= x <= n, 중복 X

# 출력
# 불가능 -> NO
# 가능 -> 한 줄에 push(+)/pop(-) 연산 출력

# 내가 못 풀고 다른 사람 아이디어 보고 품.
# https://sihyungyou.github.io/baekjoon-1874/
# 스택의 수열이 간단히 재연할 수 있는 수열이라 재현해가면서 확인 함.

import sys
from collections import deque

input = sys.stdin.readline


def solution(n, seq, sol):
    _list = []
    ans = ""
    for val in range(1, n + 1):
        _list.append(val)
        ans += "+\n"

        while len(_list) != 0 and _list[-1] == seq[0]:
            _list.pop()
            seq.popleft()
            ans += "-\n"

    if len(_list) != 0:
        ans = "NO"

    if ans == sol:
        print(True)
    else:
        print(ans)


solution(
    8,
    deque([4, 3, 6, 8, 7, 5, 2, 1]),
    "+\n+\n+\n+\n-\n-\n+\n+\n-\n+\n+\n-\n-\n-\n-\n-\n",
)

solution(
    5,
    deque([1, 2, 3, 4, 5]),
    "+\n-\n+\n-\n+\n-\n+\n-\n+\n-\n",
)

solution(
    1,
    deque([1]),
    "+\n-\n",
)
solution(
    5,
    deque([1, 2, 5, 3, 4]),
    "NO",
)
"""
"""
