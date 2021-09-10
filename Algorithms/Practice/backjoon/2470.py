import sys

input = sys.stdin.readline

N = int(input().strip())
liquid = sorted(list(map(int, input().split())))

MIN = sys.maxsize
pair = []
left, right = 0, N - 1

while left < right:
    tmp = liquid[left] + liquid[right]

    if abs(tmp) < abs(MIN):
        MIN = tmp
        pair = [liquid[left], liquid[right]]
        if MIN == 0:
            break

    if tmp > 0:
        right -= 1
    else:
        left += 1

print(*sorted(pair))
