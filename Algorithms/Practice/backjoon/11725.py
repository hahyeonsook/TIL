# REF https://www.acmicpc.net/problem/11725
# 1초, 20,000,000
# 실버 2

# 루트 없는 트리가 주어진다. 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하라.

# 입력
# 첫째 줄, N, 노드의 개수 2 <= N <= 100,000
# N-1 개 줄, 트리 상에서 연결된 두 정점

# 출력
# 2번 노드의 부모부터 차례대로 각 노드의 부모를 한 줄에 하나씩 출력

# 75% RecursionError -> 10**6으로 하니까 성공함.

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

import collections


def solution(n):
    graph = collections.defaultdict(list)
    tree = [0, 1] + [0] * (n - 1)

    # bfs O(N^2)
    def recursive_dfs(v):
        for w in graph[v]:
            # 여기서 w in discovered로 검사하면 O(N) 만큼 연산 횟수가 더해짐.
            # 그래서 시간초과..
            if tree[w] == 0:
                tree[w] = v
                recursive_dfs(w)

    # 입력
    for _ in range(n - 1):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    # DFS로 탐색
    recursive_dfs(1)

    # 출력
    for t in tree[2:]:
        print(t)


solution(int(input().strip()))
