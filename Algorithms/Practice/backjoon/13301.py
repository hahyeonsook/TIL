import sys

input = sys.stdin.readline


def solution(N):
    dp = [(1, 1)] + [(0, 0)] * (N - 1)

    for n in range(1, N):
        dp[n] = (dp[n - 1][1], sum(dp[n - 1]))

    return sum(dp[N - 1]) * 2


print(solution(int(input().strip())))
