# REF https://www.acmicpc.net/problem/2439
# 브론즈 3

import sys

input = sys.stdin.readline


def solution(n):
    for cnt in range(n):
        star = "*" * (cnt + 1)
        print(star.rjust(n))


solution(int(input().strip()))

"""
    *
   **
  ***
 ****
*****
"""
