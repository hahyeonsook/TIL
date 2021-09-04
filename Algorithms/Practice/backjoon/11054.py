import sys, bisect

input = sys.stdin.readline


def solution(N):
    arr = list(map(int, input().split()))
    increase_dp = [1] * N
    decrease_dp = [1] * N
    dp = []

    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)
            if arr[N - i - 1] > arr[N - j - 1]:
                decrease_dp[N - i - 1] = max(
                    decrease_dp[N - i - 1], decrease_dp[N - j - 1] + 1
                )
    for i in range(N):
        dytonic = increase_dp[i] + decrease_dp[i] - 1
        dp.append(max(increase_dp[i], decrease_dp[i], dytonic))
    return max(dp)


print(solution(int(input().strip())))
