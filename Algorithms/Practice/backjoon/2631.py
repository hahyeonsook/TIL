import sys

input = sys.stdin.readline


def solution(N):
    children = []
    for _ in range(N):
        children.append(int(input().strip()))
    dp = [1 for _ in range(N)]

    for i in range(N):
        for j in range(i):
            if children[i] > children[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return len(children) - max(dp)


print(solution(int(input().strip())))
