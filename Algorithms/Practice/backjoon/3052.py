import sys, collections

input = sys.stdin.readline
arr = []
for _ in range(10):
    arr.append(int(input().strip()) % 42)
print(len(collections.Counter(arr)))
