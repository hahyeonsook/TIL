import sys

input = sys.stdin.readline

N = int(input().strip())
nums = [0] * 10001
for _ in range(N):
    num = int(input().strip())
    nums[num] += 1


for num, cnt in enumerate(nums):
    for _ in range(cnt):
        sys.stdout.write(str(num) + "\n")
