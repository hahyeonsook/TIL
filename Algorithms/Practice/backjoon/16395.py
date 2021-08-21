import sys

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    dp = [[0 for r in range(N)] for c in range(N)]

    for r in range(N):
        for c in range(N):
            if c == 0 or r == c:
                dp[r][c] = 1
            else:
                dp[r][c] = dp[r - 1][c - 1] + dp[r - 1][c]

    return dp[N - 1][K - 1]


print(solution())
