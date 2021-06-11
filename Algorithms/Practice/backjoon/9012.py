# REF https://www.acmicpc.net/problem/9012
# Silver 4

# PS는 두 개의 괄호 기호인 '(',')'로 이뤄져있는 문자열이다.
# 올바른 괄호 문자열을 VPS 이라 한다.
# (ANSWK) 괄호 사이에 어떤 문자가 들어가도 짝이 맞으면 VPS이다.
# VPS인지 아닌지를 판단해서 YES/NO로 나타내라.

# 입력
# T
# 2 <= ps <= 50

# 출력
# VPS 이면 YES 아니면 NO로 한 줄에 하나씩 출력하라.

import sys

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    ps = input().strip()

    _list = []
    sol = "NO"
    # O(N), 2<=N<=50
    for p in ps:
        if p == "(":
            _list.append(p)
        elif len(_list) == 0:
            break
        else:
            _list.pop()
    else:
        if len(_list) == 0:
            sol = "YES"
    print(sol)


def solution(T, TC, ANS):

    for i in range(len(TC)):
        _list = []
        sol = "NO"
        for p in TC[i]:
            if p == "(":
                _list.append(p)
            elif len(_list) == 0:
                break
            else:
                _list.pop()

        else:
            # 모두 끝마치고 0 이 아닐 때, NO로 바꾸는 값이 없어서 오류가 있었음.
            # DEFAULT 값을 설정하는 것 중요함.
            if len(_list) == 0:
                sol = "YES"

        print(sol == ANS[i])


"""
solution(
    6,
    [
        "(())())",
        "(((()())()",
        "(()())((()))",
        "((()()(()))(((())))()",
        "()()()()(()()())()",
        "(()((())()(",
    ],
    [
        "NO",
        "NO",
        "YES",
        "NO",
        "YES",
        "NO",
    ],
)
solution(
    3,
    [
        "((",
        "))",
        "())(()",
    ],
    [
        "NO",
        "NO",
        "NO",
    ],
)
"""
