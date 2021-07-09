# REF https://www.acmicpc.net/problem/1990
# 1초, 20,000,000
# 골드 5

# 두 정수 a, b가 주어졌을 때, a 이상 b 이하인 소수인 펠린드롬을 모두 구하라.

# 입력
# a  b, 5 <= a < b <= 100,000,000

# 출력
# 오름차순으로 한 줄씩 펠린드롬을 출력하라.

# https://hminkim.github.io/algorithmpractice/2021/05/24/ap_bj_post2/ << 연구하기

import timeit
import math


def solution(a, b):
    palindrome = []

    def is_prime(number):
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    if a % 2 == 0:
        a += 1
    if b > 10000000:
        b = 10000000

    for number in range(a, b + 1, 2):
        if str(number) == str(number)[::-1]:
            if is_prime(number):
                palindrome.append(number)
    palindrome.append(-1)
    return "\n".join(map(str, palindrome))


solution(5, 100000000)

import sys

# 이건 펠레니움을 만든 후 소수인지 검사했음.
def solution(n, m):
    def isp(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 2):
            if n % i == 0:
                return False
        return True

    for i in range(len(n), len(m) + 1):
        if i % 2:
            start = 10 ** (i // 2)
            end = 10 ** (i // 2 + 1)
            for now in range(start, end):
                nttn = str(now)
                nini = nttn[:-1] + nttn[::-1]
                nownum = int(nini)
                if nownum >= int(n) and nownum <= int(m) and isp(nownum):
                    sys.stdout.write(nini)
                    sys.stdout.write("\n")
        else:
            start = 10 ** ((i // 2) - 1)
            end = 10 ** (i // 2)
            for now in range(start, end):
                nttn = str(now)
                nini = nttn + nttn[::-1]
                nownum = int(nini)
                if nownum >= int(n) and nownum <= int(m) and isp(nownum):
                    sys.stdout.write(nini)
                    sys.stdout.write("\n")
    sys.stdout.write("-1")


solution("5", "1000000")
