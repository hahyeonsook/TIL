import sys

input = sys.stdin.readline


def solution(N):
    cnt = 0
    while True:
        if N % 5 == 0:
            return cnt + (N // 5)
        N -= 3
        cnt += 1

        if N < 0:
            return -1


print(solution(int(input().strip())))
