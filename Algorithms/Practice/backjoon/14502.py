import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline


def solution(N, M):
    graph = []
    blank, virus = [], []
    for r in range(N):
        graph.append(list(map(int, input().split())))
        for c in range(M):
            if graph[r][c] == 0:
                blank.append((r, c))
            elif graph[r][c] == 2:
                virus.append((r, c))

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    def infect_virus(walls):
        visited = [[False for _ in range(M)] for _ in range(N)]
        for wr, wc in walls:
            visited[wr][wc] = True

        cnt = 0
        for sr, sc in virus:
            visited[sr][sc] = True
            queue = deque([(sr, sc)])

            while queue:
                vr, vc = queue.popleft()
                for d in range(4):
                    wr, wc = vr + dr[d], vc + dc[d]
                    if -1 < wr < N and -1 < wc < M:
                        if not visited[wr][wc] and graph[wr][wc] == 0:
                            cnt += 1

                            visited[wr][wc] = True
                            queue.append((wr, wc))
        return cnt

    safe_area = -1
    wall_list = list(permutations(blank, 3))
    for walls in wall_list:
        virus_cnt = infect_virus(walls)
        safe_area = max(safe_area, len(blank) - virus_cnt - 3)
    return safe_area


N, M = map(int, input().split())
print(solution(N, M))
