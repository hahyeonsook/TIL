import sys

input = sys.stdin.readline


def solution(N):
    s = []
    for _ in range(N):
        s.append(int(input().strip()))

    if N < 3:
        return sum(s)

    dp = [0 for _ in range(N)]
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    dp[2] = max(s[2] + s[1], s[2] + s[0])

    for i in range(3, N):
        dp[i] = max(s[i] + s[i - 1] + dp[i - 3], s[i] + dp[i - 2])
    return dp[-1]


print(solution(int(input().strip())))
