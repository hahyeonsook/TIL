# REF https://www.acmicpc.net/problem/2440
# 브론즈 3

import sys

input = sys.stdin.readline


def solution(n):
    for cnt in range(n, 0, -1):
        print("*" * cnt)


solution(int(input().strip()))
