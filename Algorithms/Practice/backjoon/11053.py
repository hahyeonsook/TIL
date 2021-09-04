import sys, bisect

input = sys.stdin.readline


def solution(N):
    lst = list(map(int, input().split()))
    dp = [1] * N

    for i in range(N):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def solution(N):
    lst = list(map(int, input().split()))
    dp = [1] * N

    for i in range(1, N):
        if lst[i - 1] < dp[i]:
            dp[i] = dp[i - 1] + 1
        else:
            for j in range(i):
                if lst[i] > lst[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def solution(N):
    lst = list(map(int, input().split()))
    dp = [lst[0]]

    for i in range(1, N):
        if lst[i] > dp[-1]:
            dp.append(lst[i])
        else:
            idx = bisect.bisect_left(dp, lst[i])
            # 저장된 값이 크면, 그 뒤로 붙으면 됨. 하지만 작으면 길이가 같은 길이이므로 소용 없음.
            dp[idx] = lst[i]
    return len(dp)


print(solution(int(input().strip())))
