import sys

input = sys.stdin.readline
A, B = input().split()
A, B = map(lambda n: int(n[::-1]), [A, B])
print(max(A, B))
