# REF https://www.acmicpc.net/problem/2447
# 실버 1

from pprint import pprint


def pattern(n):
    pass


def solution(n):
    matrix = []
    for cnt in range(n, 0, -1):
        star = ""
        if cnt == n or cnt == 1:
            star = "*" * n
        else:
            star = "* *"
        print(star)


solution(3)
