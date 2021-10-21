import sys

input = sys.stdin.readline

from collections import Counter
from itertools import product

N = int(input().strip())
A, B, C, D = [], [], [], []

for _ in range(N):
    a, b, c, d = map(int, input().split())

    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

print(Counter(list(map(sum, product(A, B, C, D))))[0])
# 시간 초과
