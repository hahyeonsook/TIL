# REF https://www.acmicpc.net/problem/1325
# 5초, 100,000,000
# 실버 2

# N개의 컴퓨터가 주어질 때, 신뢰 관계에 있는 컴퓨터들은 해킹할 수 있음
# 한 번에 가장 많은 신뢰 관계를 가진 컴퓨터 번호를 출력하라.

# 입력
# N M, 1 <= N <= 10,000 1 <= M <= 100,000
# M 개의 줄, 신뢰 관계

# 시간초과

import sys

input = sys.stdin.readline


import collections


def solution(n, m):
    graph = collections.defaultdict(list)
    visited = [False] * (n + 1)

    def recursive_dfs(v, depth=0):
        visited[v] = True
        depth += 1

        for w in graph[v]:
            if not visited[w]:
                depth = recursive_dfs(w, depth)

        return depth

    for _ in range(m):
        # s는 e를 신뢰한다. e는 s로 갈 수 있다.
        s, e = map(int, input().split())
        graph[e].append(s)

    max_v = []
    max_depth = 0
    for v in list(graph.keys()):
        visited = [False] * (n + 1)
        depth = recursive_dfs(v)

        if max_depth < depth:
            max_depth = depth
            max_v = [v]
        elif max_depth == depth:
            max_v.append(v)

    return " ".join(map(str, sorted(max_v)))


n, m = map(int, input().split())
print(solution(n, m))
