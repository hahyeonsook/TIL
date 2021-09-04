import sys, collections

input = sys.stdin.readline

A = int(input().strip())
B = int(input().strip())
C = int(input().strip())

N = A * B * C
N = collections.Counter(str(N))
for i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    if not N[i]:
        print(0)
    else:
        print(N[i])
