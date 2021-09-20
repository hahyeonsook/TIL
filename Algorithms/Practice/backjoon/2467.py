import sys

input = sys.stdin.readline
N = int(input().strip())

nums = list(map(int, input().split()))
left, right = 0, N - 1

val = [nums[left], nums[right]]

while left < right:
    tmp = nums[left] + nums[right]

    if abs(sum(val)) >= abs(tmp):
        val = [nums[left], nums[right]]

    if tmp > 0:
        right -= 1
    elif tmp < 0:
        left += 1
    else:
        break

print(*val)
