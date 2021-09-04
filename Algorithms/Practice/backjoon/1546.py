import sys

input = sys.stdin.readline
N = int(input().strip())
scores = list(map(int, input().split()))
M = max(scores)
scores = list(map(lambda s: s / M * 100, scores))
print(sum(scores) / len(scores))
