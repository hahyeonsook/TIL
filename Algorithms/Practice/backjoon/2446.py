# REF https://www.acmicpc.net/problem/2446
# 브론즈3

import sys

input = sys.stdin.readline

n = int(input().strip()) * 2 - 1

for cnt in range(n, -n, -2):
    if cnt < 0:
        cnt = -cnt + 2
    star = "*" * cnt
    print(star.center(n).rstrip() + "'")


"""
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
"""
