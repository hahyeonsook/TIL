import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().strip())
seq = defaultdict(int)
for num in input().split():
    seq[int(num)] = 1

M = int(input().strip())
nums = list(map(int, input().split()))

answer = []
for num in nums:
    answer.append(seq[num])
print(*answer)
