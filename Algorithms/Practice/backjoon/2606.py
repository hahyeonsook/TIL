# REF https://www.acmicpc.net/problem/2606
# 1초, 20,000,000
# 실버 2

# 웜 바이러스는 감염된 컴퓨터와 연결된 컴퓨터를 모두 걸리게 한다.
# 1번 컴퓨터가 감염되었을 때, 1번을 통해 바이러스에 걸리게 되는 컴퓨터의 수를 출력하라.

# 입력
# 첫째줄, n, 컴퓨터의 개수, >= 100, 컴퓨터의 번호는 1부터 시작
# 둘째줄, m, 네트워크 상에서 연결된 컴퓨터 쌍의 수
# m 개의 줄, 컴퓨터 번호 쌍

# 출력
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력

import sys

input = sys.stdin.readline

import collections


def solution(n):
    graph = collections.defaultdict(list)

    def recursive_dfs(v, discovered=[]):
        discovered.append(v)
        for w in graph[v]:
            if w not in discovered:
                discovered = recursive_dfs(w, discovered)
        return discovered

    def iterative_dfs(start_v):
        discovered = []
        stack = [start_v]
        while stack:
            v = stack.pop()
            if v not in discovered:
                discovered.append(v)
                for w in graph[v]:
                    stack.append(w)
        return discovered

    def iterative_bfs(start_v):
        discovered = [start_v]
        queue = collections.deque([start_v])
        while queue:
            v = queue.popleft()
            for w in graph[v]:
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)
        return discovered

    # 입력
    m = int(input().strip())
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    infected_r_dfs = sorted(recursive_dfs(1))
    infected_i_dfs = sorted(iterative_dfs(1))
    infected_bfs = sorted(iterative_bfs(1))

    print(infected_r_dfs == infected_i_dfs == infected_bfs)
    return False


print(solution(int(input().strip())))
