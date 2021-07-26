# REF https://www.acmicpc.net/problem/21611
# 1초, 20,000,000
# 골드 2

# 마법사 상어는 블리자드할 수 있다.
# 마법사 상어는 항상 가운데에 있다.
# 격자는 달팽이 모양으로 벽이 세워져 있다.
# 블리자드를 d, s로 실행하면, d방향으로 s만큼 폭발시킨다.
# 빈칸이 생기면 구슬들은 빈칸을 채울만큼 이동한다.
# 구슬이 4개 이상 붙어 있으면 폭발한다.
# 구슬이 폭발하고 붙으면, 변화한다.
# 연속한 구슬이 그룹을 이루고, A, B로 번식한다.
# A는 구슬의 개수, B는 그룹을 이루고 있는 구슬의 번호이다.

# 입력
# N M, N 격자의 크기 3 <= N <= 49 N은 홀수, M 블리자드를 실행한 횟수 1 <= M <= 100
# M개의 줄, d s, d 방향 1 <= d <= 4, s 거리 1 <= s <= (N-1)/2
#                      1 2 3 4 , 위 아래 왼 오

import sys
import pprint

input = sys.stdin.readline

N, M = map(int, input().split())


def snail(N):
    shell = [[0] * N for _ in range(N)]
    r = c = (N - 1) // 2

    temp = 0
    direction = 3
    content = 0
    count = 2
    # 0 1 2 3  왼 아 오 위
    while True:
        temp += 1
        for _ in range(count):
            direction = direction + 1 if direction < 3 else 0
            for _ in range(temp):
                content += 1
                if direction == 0:
                    c -= 1
                elif direction == 1:
                    r += 1
                elif direction == 2:
                    c += 1
                elif direction == 3:
                    r -= 1

                if r < 0 or c < 0:
                    return shell

                shell[r][c] = content


def solution(N, M):
    room = []
    for _ in range(N):
        line = list(map(int, input().split()))
        room.append(line)

    # 마법
    for _ in range(M):
        # 1 2 3 4 위 아래 왼 오
        d, s = map(int, input().split())

        # 블리자드
        r = c = (N - 1) // 2
        for _ in range(s):
            if d == 1:
                r -= 1
            elif d == 2:
                r += 1
            elif d == 3:
                c -= 1
            elif d == 4:
                c += 1
            room[r][c] = -1
        # 폭발
        r = (N - 1) // 2
        c = (N - 1) // 2
        temp = count = 0
        direction = 3
        number = 0
        n_position = []
        while temp < N:
            temp += 1
            count = 0
            while count < 2:
                count += 1
                direction = direction + 1 if direction < 3 else 0
                for _ in range(temp):
                    if r < 0 or c < 0:
                        break

                    if direction == 0 and c > 1:
                        c -= 1
                    elif direction == 1 and r < N - 2:
                        r += 1
                    elif direction == 2 and c < N - 2:
                        c += 1
                    elif direction == 3 and r > 1:
                        r -= 1

                    if room[r][c] == -1:
                        continue
                    elif number != room[r][c]:
                        number = room[r][c]
                        n_position = [(r, c)]
                    else:
                        n_position.append((r, c))
                        if len(n_position) == 4:
                            for p in n_position:
                                room[p[0]][p[1]] = -1
        # 달팽이 이동
        flat_room = [e for arr in room for e in arr]
        pprint.pprint(flat_room)


solution(N, M)
# print(snail(7))
