# REF https://www.acmicpc.net/problem/1913
# 2초, 40,000,000
# 실버 5

# 홀수인 자연수 N이 주어질 때, NxN 행렬에 N^2까지 달팽이 모양으로 숫자를 채워라.

# 입력
# N, 3 <= N <= 999
# 좌표를 찾을 숫자

from pprint import pprint
import sys

input = sys.stdin.readline


def solution(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    target = int(input().strip())

    num = n ** 2
    # 0 아 1 오 2 위 3 왼
    count, scope = n, 1
    direction = 0
    r, c = -1, 0
    while num > 0:
        for _scp in range(scope):
            for _cnt in range(count):
                # 아
                if direction == 0 and r < n:
                    r += 1
                # 오
                elif direction == 1 and c < n:
                    c += 1
                # 위
                elif direction == 2 and r > 0:
                    r -= 1
                # 왼
                elif direction == 3 and c > 0:
                    c -= 1

                matrix[r][c] = num
                if num == target:
                    matrix.append([r + 1, c + 1])
                num -= 1

            direction = 0 if direction > 2 else direction + 1

        count -= 1

        if scope == 1:
            scope = 2

    for r in range(len(matrix)):
        print(" ".join(map(str, matrix[r])))


solution(int(input().strip()))
