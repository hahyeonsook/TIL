# REF https://www.acmicpc.net/problem/2075
# 1초, 20,000,000
# 골드 5

# NxN의 표에 N^2의 수가 채워져 있다.
# 모든 수는 자신의 한 칸 위에 있는 수보다 크다.
# N번째 큰 수를 찾는 프로그램을 작성하라.

# 입력
# N, 1 <= N <= 1,500
# -10억 <= N[i][j] <= 10억

# 메모리 초과

import sys

input = sys.stdin.readline
n = int(input().strip())
nums = []

import heapq


def heap_insert(x):
    x = int(x)
    min_v = nums[0] if nums else None
    if not min_v or min_v < x:
        if len(nums) > n - 1:
            heapq.heappop(nums)
        heapq.heappush(nums, x)


for _ in range(n):
    list(map(heap_insert, input().split()))

print(heapq.heappop(nums))
