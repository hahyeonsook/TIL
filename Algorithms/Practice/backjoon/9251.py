import sys, pprint

input = sys.stdin.readline
A = " " + input().strip()
B = " " + input().strip()

C, R = len(A), len(B)
dp = [[0 for _ in range(C)] for _ in range(R)]
for r in range(1, R):
    for c in range(1, C):
        if A[c] == B[r]:
            dp[r][c] = dp[r - 1][c - 1] + 1
        else:
            dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

print(dp[-1][-1])
