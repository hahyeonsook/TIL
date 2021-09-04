import sys

input = sys.stdin.readline


def solution():
    N = int(input().strip())

    max_dp = [0] * 3
    min_dp = [0] * 3

    max_tmp = [0] * 3
    min_tmp = [0] * 3

    for _ in range(N):
        a, b, c = map(int, input().split())

        max_tmp[0] = a + max(max_dp[0], max_dp[1])
        min_tmp[0] = a + min(min_dp[0], min_dp[1])

        max_tmp[1] = b + max(max_dp[0], max_dp[1], max_dp[2])
        min_tmp[1] = b + min(min_dp[0], min_dp[1], min_dp[2])

        max_tmp[2] = c + max(max_dp[1], max_dp[2])
        min_tmp[2] = c + min(min_dp[1], min_dp[2])

        max_dp = max_tmp[:]
        min_dp = min_tmp[:]

    return [max(max_dp), min(min_dp)]


print(*solution())
