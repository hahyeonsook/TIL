import sys

input = sys.stdin.readline


def solution(N, M):
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, list(input().strip()))))

    n = 0
    dp = [[0 for _ in range(M)] for _ in range(N)]
    for r in range(N):
        for c in range(M):
            dp[r][c] = matrix[r][c]
            if r != 0 and c != 0 and dp[r][c] != 0:
                dp[r][c] += min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])

            n = max(n, dp[r][c])

    return n ** 2


N, M = map(int, input().split())
print(solution(N, M))
