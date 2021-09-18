import sys

input = sys.stdin.readline

N = int(input().strip())

nums = list(map(int, input().split()))
sorted_nums = sorted(list(set(nums)))
dict_nums = {num: idx for idx, num in enumerate(sorted_nums)}

answer = []
for num in nums:
    answer.append(dict_nums[num])
print(*answer)
