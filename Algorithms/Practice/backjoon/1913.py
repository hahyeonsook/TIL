# https://www.acmicpc.net/problem/1913
# 2초 40,000,000

# 홀수인 자연수 N이 주어지면 1~N^2까지의 자연수를 달팽이 모양으로 N*N 표에 채울 수 있다.

# 입력
# 3 <= N <= 999
# n <= N^2

# 출력
# N*N 표와 주어진 좌표에 들어갈 자연수를 출력하라.

sol1 = "49 26 27 28 29 30 31\n\
48 25 10 11 12 13 32\n\
47 24 9 2 3 14 33\n\
46 23 8 1 4 15 34\n\
45 22 7 6 5 16 35\n\
44 21 20 19 18 17 36\n\
43 42 41 40 39 38 37"
sol2 = "5 7"

import sys


def solution(n, m):
    matrix = [[0] * n for _ in range(n)]
    nums = [i + 1 for i in range(n * n)]
    x = y = 0
    step = 1

    while nums:
        while x < n - 1 and matrix[x][y] == 0:
            matrix[x][y] = nums.pop()
            x += step
        x, y = y, x
        step *= -1

    return matrix


ans1, ans2 = solution(5, 6)
for i in range(len(ans1)):
    for j in range(len(ans1)):
        print(ans1[i][j], end=" ")
    print()
# print((ans1, ans2) == (sol1, sol2))
