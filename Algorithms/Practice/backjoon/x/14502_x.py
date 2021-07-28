# REF https://www.acmicpc.net/problem/14502
# 2초, 40,000,000
# 골드 5
from pprint import pprint
import sys

input = sys.stdin.readline

import collections
from itertools import combinations


def solution(n, m):
    graph = collections.defaultdict(list)
    empty = []
    virus = []

    def bfs(virus, walls):
        count = len(virus)
        visited = [False] * (n * m + 1)
        for vir in virus:
            queue = collections.deque([vir])
            while queue:
                v = queue.popleft()
                for w in graph[v]:
                    if not visited[w] and w not in list(walls):
                        visited[w] = True
                        queue.append(w)
                        count += 1
        return count

    tmp = []
    for _ in range(n):
        row = list(map(int, input().split()))
        tmp.append(row)

    node = 0
    for r in range(n):
        for c in range(m):
            node += 1
            if tmp[r][c] == 1:
                continue

            if tmp[r][c] == 2:
                virus.append(node)
            else:
                empty.append(node)
            if r > 0 and tmp[r - 1][c] != 1:
                graph[node].append(node - m)
            if r < n - 1 and tmp[r + 1][c] != 1:
                graph[node].append(node + m)
            if c > 0 and tmp[r][c - 1] != 1:
                graph[node].append(node - 1)
            if c < m - 1 and tmp[r][c + 1] != 1:
                graph[node].append(node + 1)

    combs = list(combinations(empty, 3))
    min_virus = n * m
    for comb in combs:
        min_virus = min(min_virus, bfs(virus, comb))

    print(min_virus)


n, m = map(int, input().split())
solution(n, m)
