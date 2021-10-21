def solution():
    import sys

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

def solution():
    A = input().strip()
    B = input().strip()
    dp = [0] * (len(B) + 1)

    for char1 in A:
        cnt = 0
        for idx, char2 in enumerate(B):
            if char1 == char2:
                dp[idx], cnt = cnt + 1, dp[idx]
            else:
                dp[idx], cnt = max(dp[idx - 1], dp[idx]), dp[idx]
    print(dp[-2])
