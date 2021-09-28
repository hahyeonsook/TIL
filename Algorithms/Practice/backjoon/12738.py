import sys

input = sys.stdin.readline

N = int(input().strip())
seq = list(map(int, input().split()))

import bisect

dp = [seq[0]]
for num in seq[1:]:
    if num > dp[-1]:
        dp.append(num)
    else:
        idx = bisect.bisect_left(dp, num)
        dp[idx] = num

print(len(dp))
