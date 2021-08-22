import sys

input = sys.stdin.readline


def solution(N):
    dp = [[0 for _ in range(10)] for _ in range(101)]

    dp[1] = [0] + [1 for i in range(1, 10)]
    dp[2] = [1, 1] + [2 for i in range(2, 9)] + [1]

    for r in range(3, N + 1):
        dp[r][0] = dp[r - 1][1]
        dp[r][9] = dp[r - 1][8]

        for c in range(1, 9):
            dp[r][c] = dp[r - 1][c - 1] + dp[r - 1][c + 1]

    return sum(dp[N]) % 1000000000


print(solution(int(input().strip())))
