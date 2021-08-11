# 5부 알고리즘/정렬

from typing import List


def majorityElement(nums: List[int]) -> int:
    for num in nums:
        if nums.count(num) > len(num):
            return num


from collections import defaultdict


def majorityElement(nums: List[int]) -> int:
    counts = defaultdict(int)
    for num in nums:
        if counts[num] == 0:
            counts[num] = nums.count(num)

        if counts[num] > len(nums) // 2:
            return num


def majorityElement(nums: List[int]) -> int:
    # 1. 분할 -> a, b는 각각 최소 단위로 쪼개질 것임. 그렇게 하기 위해서는 상단에 끊어서 리턴해주는 부분이 필요.
    # 끊어서 리턴
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    # 최소 단위로 쪼갬
    half = len(nums) // 2
    a = majorityElement(nums[:half])
    b = majorityElement(nums[half:])
    # 3. 정복 -> a가 과반수라면, [b, a][1]이 되어 a를 리턴할 것이고, 아니면 b를 리턴할 것이다.
    # 비둘기집 원리⭐
    return [b, a][nums.count(a) > half]


nums = [2, 2, 1, 1, 1, 2, 2]
majorityElement(nums)


def majorityElement(nums: List[int]) -> int:
    # 정렬하여 가운데를 지정하면 반드시 과반수 이상인 엘리먼트일 것이다.
    return sorted(nums)[len(nums) // 2]


def diftWaysToCompute(input: str) -> List[int]:
    def compute(left, right, op):
        results = []
        for l in left:
            for r in right:
                results.append(eval(str(l) + op + str(r)))
        return results

    if input.isdigit():
        return [int(input)]

    results = []
    for index, value in enumerate(input):
        if value in "-+*":
            left = diftWaysToCompute(input[:index])
            right = diftWaysToCompute(input[index + 1 :])

            results.extend(compute(left, right, value))

    return results


# 브루투 포스
def fib(N: int) -> int:
    if N <= 1:
        return N

    return fib(N - 1) + fib(N - 2)


# 메모이제이션, 하향식
import collections


def solution():
    dp = collections.defaultdict(int)

    def fib(N: int) -> int:
        if N <= 1:
            return N

        if dp[N]:
            return dp[N]

        dp[N] = fib(N - 1) + dp(N - 2)
        return dp[N]


# 타뷸레이션, 상향식
# 재귀를 사용하지 않고, 반복적으로 풀이히며, 작은 값부터 직접 계산하면서 타뷸레이션한다.
def solution():
    dp = collections.defaultdict(int)

    def fib(N: int) -> int:
        dp[0] = 1
        dp[1] = 1

        for i in range(2, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[N]


def fib(N: int) -> int:
    x, y = 0, 1
    for _ in range(0, N):
        x, y = y, x + y
    return x


def zero_one_knapsack(cargo):
    capacity = 15
    pack = []

    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i - 1][1] <= c:
                pack[i].append(
                    max(
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                        pack[i - 1][c],
                    )
                )
            else:
                pack[i].append(pack[i - 1][c])
