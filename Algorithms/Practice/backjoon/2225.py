import sys

input = sys.stdin.readline


def solution(N, K):
    mod = 1000000000
    dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

    for r in range(K + 1):
        for c in range(N + 1):
            if r < 2:
                dp[r][c] = r
            else:
                dp[r][c] = (dp[r - 1][c] + dp[r][c - 1]) % mod

    return dp[K][N]


N, K = map(int, input().split())
print(solution(N, K))
