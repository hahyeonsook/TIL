# 플로이드 와샬
# 29452kb 156ms
from itertools import product


def solution(N):
    maps = [list(map(int, input().split())) for _ in range(N)]

    for k, u, v in product(range(N), repeat=3):
        if maps[u][v] == 0 and maps[u][k] == 1 and maps[k][v] == 1:
            maps[u][v] = 1

    for m in maps:
        print(*m)


# bfs
# 31872kb 172ms
from collections import defaultdict, deque


def solution(N):
    maps = [list(map(int, input().split())) for _ in range(N)]

    answer = [[0 for _ in range(N)] for _ in range(N)]

    def bfs(start_v):
        visited = [False for _ in range(N)]
        queue = deque([start_v])
        while queue:
            v = queue.popleft()
            for w in range(N):
                if maps[v][w] == 1 and not visited[w]:
                    queue.append(w)
                    visited[w] = True
                    answer[start_v][w] = 1
        return

    for v in range(N):
        bfs(v)
        print(*answer[v])

#https://www.acmicpc.net/source/33614642
# 32932kb 108ms
from collections import deque, defaultdict


def solution(N):
    maps = [list(map(int, input().split())) for _ in range(N)]

    graph = defaultdict(list)
    for r in range(N):
        graph[r] = [c for c in range(N) if maps[r][c] == 1]

    def bfs(start_v):
        visited = [0 for _ in range(N)]
        queue = deque([start_v])
        while queue:
            v = queue.popleft()
            for w in graph[v]:
                if visited[w] == 0:
                    queue.append(w)
                    visited[w] = 1
        return visited

    for v in range(N):
        print(*bfs(v))


if __name__ == "__main__":
    solution(int(input().strip()))
