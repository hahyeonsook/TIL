# REF https://www.acmicpc.net/problem/14425
# 2초, 40,000,000
# 실버 3

# N개의 문자열로 이루어진 집합 S가 주어짐
# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되는 것이 총 몇개인지 구하라.

# 입력
# N M, 문자열의 개수 N 문자열의 개수 M 1 <= N, M <= 10,000
# N개의 줄, S에 포함되는 문자열들
# M개의 줄, 검사해야하는 문자열들
# 입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있음.

# 출력
# S에 몇개가 포함되어 있는지 출력하라.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def solution(n, m):
    s = set()
    count = 0
    for _ in range(n):
        string = input().strip()
        s.add(string)

    for _ in range(m):
        test = input().strip()
        if test in s:
            count += 1
    return count


print(solution(n, m))
