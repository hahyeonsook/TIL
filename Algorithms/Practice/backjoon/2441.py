# REF https://www.acmicpc.net/problem/2441
# 브론즈 3

import sys

input = sys.stdin.readline
n = int(input().strip())

for cnt in range(n, 0, -1):
    star = "*" * cnt
    print(star.rjust(n))

"""
*****
 ****
  ***
   **
    *
"""
