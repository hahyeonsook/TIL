# REF https://www.acmicpc.net/problem/10994
# 실버 4

# 입력
# N, 1 <= N <= 100

# 등차수열
# a + r(n-1), 4n-3

# 출력
# 400*400, 3256 byte
import sys

input = sys.stdin.readline


def solution(N):
    size = 4 * N - 3
    # O(N*N), 160,000
    matrix = [[" " for _ in range(4 * N - 3)] for _ in range(4 * N - 3)]

    for s in range(0, ((size // 2) + 1), 2):
        e = size - s

        d = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        x = s
        y = s - 1
        while d < 4:
            if (
                s - 1 < x + dx[d % 4] < e
                and s - 1 < y + dy[d % 4] < e
                and matrix[x + dx[d % 4]][y + dy[d % 4]] == " "
            ):
                x += dx[d % 4]
                y += dy[d % 4]
                matrix[x][y] = "*"
            else:
                d += 1

    for x in range(len(matrix)):
        print("".join(map(str, matrix[x])))


solution(int(input().strip()))
