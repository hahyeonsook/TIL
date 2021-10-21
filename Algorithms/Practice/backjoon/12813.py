import sys

input = sys.stdin.readline
A = list(map(int, input().strip()))
B = list(map(int, input().strip()))

N = len(A)

for idx in range(N):
    print(A[idx] & B[idx], end="")
print()

for idx in range(N):
    print(A[idx] | B[idx], end="")
print()

for idx in range(N):
    print(A[idx] ^ B[idx], end="")
print()

for idx in range(N):
    print(1 if A[idx] == 0 else 0, end="")
print()

for idx in range(N):
    print(1 if B[idx] == 0 else 0, end="")
print()
