import sys

input = sys.stdin.readline


def solution(K):
    dp = [(1, 0)] + [(0, 0)] * K

    for k in range(1, K + 1):
        dp[k] = (dp[k - 1][1], dp[k - 1][0] + dp[k - 1][1])

    return dp[k]


print(*solution(int(input().strip())))
