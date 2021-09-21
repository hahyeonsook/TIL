import sys

input = sys.stdin.readline

N = int(input().strip())
nums = sorted(list(map(int, input().split())))

left, right = 0, N - 1
answer = []

for idx in range(N - 2):
    left, right = idx + 1, N - 1
    while left < right:
        tmp = nums[idx] + nums[left] + nums[right]

        if not answer or abs(tmp) <= abs(sum(answer)):
            answer = [nums[idx], nums[left], nums[right]]

        if tmp > 0:
            right -= 1
        elif tmp < 0:
            left += 1
        else:
            idx = -1
            break

    if idx < 0:
        break


print(*answer)
