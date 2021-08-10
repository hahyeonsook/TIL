# REF https://www.acmicpc.net/problem/2579
# 1초, 20,000,000
# 실버3

# 계단 아래 시작점부터 꼭대기에 위치한 도착점까지 간다.
# 계단을 밟으면 그 계단의 점수를 얻게 된다.
# 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하라.

# 계단 오르는 규칙
# 1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
# 2. 연속된 세 개의 계단을 모두 밟아서는 안된다.
# 3. 마지막 도착 계단은 반드시 밟아야 한다.

# 입력
# N, 계단의 개수, 0 <= N <= 300
# N개의 줄, 계단에 쓰여있는 점수, 0 <= N[i] <= 10,000

import sys

input = sys.stdin.readline

# 상향식
def solution(N):
    steps = []
    for _ in range(N):
        steps.append(int(input().strip()))
    dp = [0] * (N + 1)
    dp[0] = steps[0]
    dp[1] = steps[0] + steps[1]
    dp[2] = max(steps[1] + steps[2], steps[0] + steps[2])
    for i in range(3, N):
        dp[i] = max(dp[i - 3] + steps[i - 1] + steps[i], dp[i - 2] + steps[i])

    return dp[N - 1]


print(solution(int(input().strip())))
