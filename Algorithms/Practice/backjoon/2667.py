# REF https://www.acmicpc.net/problem/2667
# 1초, 20,000,000
# 실버 1

# 반례
# https://www.acmicpc.net/board/view/71535
import sys, pprint

input = sys.stdin.readline


import collections


def solution(n):
    graph = collections.defaultdict(list)
    homes = [False] * (n ** 2 + 1)

    def bfs(start_v):

        if homes[start_v]:
            return 0

        homes[start_v] = True
        discovered = [start_v]
        queue = collections.deque([start_v])
        while queue:
            v = queue.popleft()
            for w in graph[v]:
                if not homes[w]:
                    homes[w] = True
                    queue.append(w)
                    discovered.append(w)
        return len(discovered)

    tmp = []
    for _ in range(n):
        row = list(map(int, [s for s in input().strip()]))
        tmp.append(row)

    node = 0
    for r in range(n):
        for c in range(n):
            node += 1
            if tmp[r][c] == 1:
                graph[node] = []
                if r > 0 and tmp[r - 1][c] == 1:
                    graph[node].append(node - n)
                if r < n - 1 and tmp[r + 1][c] == 1:
                    graph[node].append(node + n)
                if c > 0 and tmp[r][c - 1] == 1:
                    graph[node].append(node - 1)
                if c < n - 1 and tmp[r][c + 1] == 1:
                    graph[node].append(node + 1)

    group_cnt = []
    for node in list(graph.keys()):
        cnt = bfs(node)
        if cnt > 0:
            group_cnt.append(cnt)

    print(len(group_cnt))
    print("\n".join(map(str, sorted(group_cnt))))


solution(int(input().strip()))
