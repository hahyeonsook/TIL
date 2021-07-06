# 진짜 약수로 숫자를 구하는 것은 가장 작은 값과 가장 큰 값을 곱하면 된다.
import sys

input = sys.stdin.readline
n = int(input().strip())
nums = list(map(int, input().split()))
print(min(nums) * max(nums))
