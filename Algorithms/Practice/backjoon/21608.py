# REF https://www.acmicpc.net/problem/21608
# 1초, 20,000,000
# 실버 1

# 교실은 NxN 격자로 나타낼 수 있다.
# 학교에 다니는 학생 수는 N^2다.
# (r, c)는 r행 c열
# |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸인 (r1, c1)과 (r2, c2)를 인접하다고 한다.
# 다음과 같은 규칙을 이용해 학생의 자리를 정하려고 한다.
# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로,
#    그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
# 학생의 만족도는 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구하면 된다.
# 자리를 모두 정한 후 학생의 만족도의 총 합을 구하라.

# 입력
# N, 3 <= N <= 20
# N^2개의 줄, 자리를 정할 순서대로 주어진다.
# 학생의 번호 좋아하는 학생 * 4
# 학생의 번호와 좋아하는 학생들은 중복되지 않는다.
# 자기 자신을 좋아하는 경우는 없다.

# 출력
# 만족도의 총 합을 출력한다.

import sys

input = sys.stdin.readline
N = int(input().strip())

from collections import defaultdict


def solution(N):
    room = [[-1] * N for _ in range(N)]
    like_dict = defaultdict(list)
    for _ in range(N * N):
        student, like0, like1, like2, like3 = map(int, input().split())
        like_dict[student] = [like0, like1, like2, like3]

        max_position = [-1, -1]
        max_score = -1
        for r in range(N):
            for c in range(N):
                if room[r][c] > -1:
                    continue
                score = 0
                if r > 0:
                    if room[r - 1][c] in like_dict[student]:
                        score += 10
                    if room[r - 1][c] < 0:
                        score += 1
                if c > 0:
                    if room[r][c - 1] in like_dict[student]:
                        score += 10
                    if room[r][c - 1] < 0:
                        score += 1
                if r < N - 1:
                    if room[r + 1][c] in like_dict[student]:
                        score += 10
                    if room[r + 1][c] < 0:
                        score += 1
                if c < N - 1:
                    if room[r][c + 1] in like_dict[student]:
                        score += 10
                    if room[r][c + 1] < 0:
                        score += 1

                if max_score < score:
                    max_score = score
                    max_position = [r, c]
        room[max_position[0]][max_position[1]] = student

    score = 0
    for r in range(N):
        for c in range(N):
            like = 0
            student = room[r][c]
            if r > 0 and room[r - 1][c] in like_dict[student]:
                like += 1
            if c > 0 and room[r][c - 1] in like_dict[student]:
                like += 1
            if r < N - 1 and room[r + 1][c] in like_dict[student]:
                like += 1
            if c < N - 1 and room[r][c + 1] in like_dict[student]:
                like += 1

            if like > 0:
                score += 10 ** (like - 1)
    print(score)


solution(N)
