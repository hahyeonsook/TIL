# 시간초과
import sys

input = sys.stdin.readline
n = int(input().strip())
ns = list(map(int, input().split())).sort()
m = int(input().strip())
ms = list(map(int, input().split()))

for m in ms:
    if m in ns:
        print(1)
    else:
        print(0)
