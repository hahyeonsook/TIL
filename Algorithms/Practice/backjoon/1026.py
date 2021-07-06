from functools import reduce
import sys

input = sys.stdin.readline

n = int(input().strip())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

print(sum([a[i] * b[i] for i in range(n)]))
