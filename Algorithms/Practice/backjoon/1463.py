import sys

input = sys.stdin.readline


def solution(N):
    dp = [0, 0, 1, 1] + [0] * (N - 3)

    for n in range(4, N + 1):
        tmp = [dp[n - 1] + 1]
        if n % 2 == 0:
            tmp.append(dp[n // 2] + 1)
        if n % 3 == 0:
            tmp.append(dp[n // 3] + 1)

        dp[n] = min(tmp)

    return dp[N]


print(solution(int(input().strip())))
