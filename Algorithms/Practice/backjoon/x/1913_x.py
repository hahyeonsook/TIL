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


def solution(n, find):
    snail = [[0] * n for i in range(n)]
    value = 1
    direc = 1
    count = 1
    xtemp = int((n - 1) // 2)
    ytemp = int((n - 1) // 2)
    snail[xtemp][ytemp] = value

    while value != n * n:
        if direc == 1:
            for i in range(count):
                value += 1
                xtemp -= 1
                snail[xtemp][ytemp] = value
                if value == n * n:
                    break
            direc = 2
        elif direc == 2:
            for i in range(count):
                value += 1
                ytemp += 1
                snail[xtemp][ytemp] = value
            count += 1
            direc = 3
        elif direc == 3:
            for i in range(count):
                value += 1
                xtemp += 1
                snail[xtemp][ytemp] = value
            direc = 4

        elif direc == 4:
            for i in range(count):
                value += 1
                ytemp -= 1
                snail[xtemp][ytemp] = value
            count += 1
            direc = 1

    for i in range(n):
        for j in range(n):
            print(snail[i][j], end=" ")
            if snail[i][j] == find:
                save_x = i + 1
                save_y = j + 1
        print()
    print(save_x, save_y)


# https://egg-money.tistory.com/85


solution(5, 6)
# print((ans1, ans2) == (sol1, sol2))
