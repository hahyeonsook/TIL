import sys

input = sys.stdin.readline


def solution():
    A = " " + input().strip()
    B = " " + input().strip()
    N, M = len(A), len(B)
    # dp[i][j] = A[i]번째 글자까지와 B[j]번째 글자까지 비교했을 때의 LCS
    dp = [[0] * N for _ in range(M)]
    b = 0
    for i in range(1, N):
        for j in range(1, M):
            if A[i] == B[j]:
                dp[i][j] = dp[i][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


print(solution())
