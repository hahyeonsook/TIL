import sys

input = sys.stdin.readline
N = int(input().strip())
S = list(map(int, input().strip()))
print(sum(S))
