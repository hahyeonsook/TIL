# REF https://www.acmicpc.net/problem/1935
# Sliver 3
# 2초 40,000,000 연산 안에 끝내야 함.


# 후위 표기식으로 표기된 식이 주어졌을 때, 계산하라

# 입력
# 첫번 째 줄, 피연산자 개수, 1 <= n <= 26
# 두번 째 줄, 후위 표기식, A~Z, len(표기식) < 100
# N+2번 째 줄, 피연산자 값


# 출력
# 소숫점 둘째 자리까지 출력

import sys
from collections import deque
from string import ascii_uppercase


input = sys.stdin.readline

n = int(input().strip())

notation = input().strip()

alpha_list = list(ascii_uppercase)[:n]
operands = dict()
for i in range(n):
    operands[alpha_list[i]] = int(input().strip())


_list = deque()
for op in notation:
    if op in alpha_list:
        _list.append(operands[op])
    else:
        operand2 = _list.pop()
        operand1 = _list.pop()

        if op == "+":
            _list.append(operand1 + operand2)
        elif op == "-":
            _list.append(operand1 - operand2)
        elif op == "/":
            _list.append(operand1 / operand2)
        elif op == "*":
            _list.append(operand1 * operand2)

print("{:.2f}".format(_list.pop()))


def solution(n, notation, operand):
    alpha_list = list(ascii_uppercase)[:n]
    operands = dict()
    for i in range(len(operand)):
        operands[alpha_list[i]] = operand[i]

    _list = deque()
    for s in notation:
        if s in alpha_list:
            _list.append(operands[s])
        else:
            operand2 = _list.pop()
            operand1 = _list.pop()
            operand3 = 0
            if s == "+":
                operand3 = operand1 + operand2
            elif s == "-":
                operand3 = operand1 - operand2
            elif s == "/":
                operand3 = operand1 / operand2
            elif s == "*":
                operand3 = operand1 * operand2

            _list.append(operand3)

    print("{:.2f}".format(_list.pop()))


# solution(5, "ABC*+DE/-", [1, 2, 3, 4, 5])
# solution(1, "AA+A+", [1])
# solution(1, "A", [1])
# solution(1, "AAA--", [1])
# solution(1, "AAA--", [-1])
