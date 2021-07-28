# REF https://www.acmicpc.net/problem/2178
# 1초, 20,000,000
# 실버 1

# NxM 크리의 배열로 표현된 미로가 있을 때,
# 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 이 때, (1, 1)에서 (N, M)으로 이동할 때 지나야 하는 최소의 칸 수를 구하라.

# 입력
# N M, 2 <= N, M <= 100
# N 개의 줄, M크기의 str, 각 수는 붙어서 입력으로 주어짐

import sys, pprint

input = sys.stdin.readline

import collections


def solution(n, m):
    graph = collections.defaultdict(list)

    def bfs(start_v):
        dist = [0, 1] + ([-1] * (n * m - 1))
        queue = collections.deque([start_v])
        while queue:
            v = queue.popleft()
            for w in graph[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    queue.append(w)
        return dist[-1]

    tmp = []
    for _ in range(n):
        row = list(map(int, str(int(input().strip()))))
        tmp.append(row)
    node = 0
    # 왜 두 번 넣으면 중복되는걸까
    for r in range(n):
        for c in range(m):
            node += 1
            if tmp[r][c] == 1:
                # 위
                if r > 0 and tmp[r - 1][c] == 1:
                    graph[node].append(node - m)
                # 아래
                if r < n - 1 and tmp[r + 1][c] == 1:
                    graph[node].append(node + m)
                # 왼
                if c > 0 and tmp[r][c - 1] == 1:
                    graph[node].append(node - 1)
                # 오
                if c < m - 1 and tmp[r][c + 1] == 1:
                    graph[node].append(node + 1)
    # pprint.pprint(graph)
    return bfs(1)


import sys

input = sys.stdin.readline

import collections


def solution2(n, m):
    graph = collections.defaultdict(list)

    def bfs(start_v):
        dist = [0, 1] + ([-1] * (n * m - 1))
        queue = collections.deque([start_v])
        while queue:
            v = queue.popleft()
            for w in graph[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    if w == n * m:
                        return dist[w]
                    queue.append(w)

    tmp = []
    for _ in range(n):
        row = list(map(int, [s for s in input().strip()]))
        tmp.append(row)

    node = 0
    for r in range(n):
        for c in range(m):
            node += 1
            if tmp[r][c] == 1:
                if r > 0 and tmp[r - 1][c] == 1:
                    graph[node].append(node - m)
                if r < n - 1 and tmp[r + 1][c] == 1:
                    graph[node].append(node + m)
                if c > 0 and tmp[r][c - 1] == 1:
                    graph[node].append(node - 1)
                if c < m - 1 and tmp[r][c + 1] == 1:
                    graph[node].append(node + 1)

    return bfs(1)


n, m = map(int, input().split())
print(solution2(n, m))
