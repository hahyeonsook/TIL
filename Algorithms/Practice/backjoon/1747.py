# REF https://www.acmicpc.net/problem/1747
# 2초, 40,000,000
# 골드 5

# N보다 크거나 같고, 소수이면서 펠린드롬인 수 중에서 가장 작은 수를 구하라.

# 입력
# N 1 <= N <= 1,000,000

# 출력
# 조건을 만족하는 수를 출력하라.

import sys

input = sys.stdin.readline
# start_number = int(input().strip())

import math


def solution(start_number):
    def isPrime(number):
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    if start_number < 2:
        start_number += 1

    for number in range(start_number, 1005000):
        if str(number) == str(number)[::-1]:
            if isPrime(number):
                return number


print(solution(1))
print(solution(2))
print(solution(31))
