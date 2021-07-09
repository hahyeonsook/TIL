# REF https://www.acmicpc.net/problem/2407
# 2초, 40,000,000

# nCm을 출력하라.

# 입력
# n, 5 <= n <= 100
# m, 5 <= m <= 100
# m <= n

from math import factorial


def solution(n, m):
    print(factorial(n) // (factorial(m) * factorial(n - m)))


solution(100, 6)
