import sys

input = sys.stdin.readline


def solution(N):
    dp = [0, 1, 1] + [0] * (N - 2)

    for n in range(2, N + 1):
        dp[n] = dp[n - 1] + dp[n - 2]

    return dp[N]


print(solution(int(input().strip())))
