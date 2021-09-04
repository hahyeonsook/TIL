import sys

input = sys.stdin.readline

idx, max_num = 0, 0
for i in range(9):
    num = int(input().strip())
    if num > max_num:
        idx = i
        max_num = num

print(max_num)
print(idx + 1)
