import sys, collections
from typing import overload

input = sys.stdin.readline


def solution(N):
    parent_nodes = list(map(int, input().split()))
    remove_node = int(input().strip())

    start_v = -1
    graph = {i: [] for i in range(N)}
    for node, parent in enumerate(parent_nodes):
        if parent == -1:
            start_v = node
            continue
        if parent != remove_node and node != remove_node:
            graph[parent].append(node)

    def dfs(start_v):
        visited = [False for _ in range(N)]
        queue = [start_v]

        if start_v == remove_node:
            return 0

        cnt = 0
        while queue:
            v = queue.pop()
            if not visited[v]:
                visited[v] = True
                if not graph[v]:
                    cnt += 1
                for w in graph[v]:
                    queue.append(w)
        return cnt

    return dfs(start_v)


print(solution(int(input().strip())))
