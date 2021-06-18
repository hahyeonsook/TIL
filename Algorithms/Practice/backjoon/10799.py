# REF https://www.acmicpc.net/problem/10799
# Silver 3
# 1초, 20,000,000

# 여러 개의 쇠막대기를 겹쳐놓고 레이저로 절단한다.
# 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
# 단, 위에 놓인 쇠막대는 아래에 놓인 쇠막대에 완전히 포함되고, 끝점이 겹치지 않아야 한다.
# 각 쇠막대를 자르는 레이저는 적어도 1개 존재한다.
# 레이저는 어떤 쇠막대기의 끝점과도 겹치지 않는다.
# 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍으로 표현된다. 모든 '()'는 반드시 레이저다.
# 쇠막대기의 왼쪽 끝은 여는 괄오 '(' 오른쪽 끝은 닫힌 괄호 ')'로 표현한다.
# 이때 잘려진 쇠막대기 조각의 총 개수를 구하라.

# 입력
# 괄호 표현이 공백없이 주어짐, len(괄호) <= 100,000

# 출력
# 잘려진 조각의 총 개수를 나타내는 정수를 출력

import sys

input = sys.stdin.readline

string = input().strip()
_list = []
index = 0
cnt = 0

while index != len(string):
    if string[index : index + 2] == "()":
        cnt += len(_list)
        index += 1
    elif string[index] == "(":
        _list.append("(")
    elif string[index] == ")":
        _list.pop()
        cnt += 1
    index += 1

print(cnt)


def solution(string, sol):
    _list = []
    cnt = 0
    i = 0

    while i != len(string):
        if string[i : i + 2] == "()":
            cnt += len(_list)
            i += 1
        elif string[i] == "(":
            _list.append("(")
        elif string[i] == ")":
            _list.pop()
            cnt += 1
        i += 1

    if len(_list) != 0:
        cnt += len(_list)

    if sol == cnt:
        print("True")
    else:
        print(cnt)


solution("()(((()())(())()))(())", 17)
solution("(((()(()()))(())()))(()())", 24)
solution("(())", 2)
solution("()()", 0)
