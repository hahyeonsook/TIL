# REF https://www.acmicpc.net/problem/11725
# 1초, 20,000,000
# 실버 2

# 루트 없는 트리가 주어진다. 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하라.

# 입력
# 첫째 줄, N, 노드의 개수 2 <= N <= 100,000
# N-1 개 줄, 트리 상에서 연결된 두 정점

# 출력
# 2번 노드의 부모부터 차례대로 각 노드의 부모를 한 줄에 하나씩 출력

import sys

input = sys.stdin.readline


def solution(n):
    graph = {i + 1: [] for i in range(n)}
    tree = [None] * (n + 1)

    def dfs(node: int):

        while graph[node]:
            child = graph[node].pop()

            if child != 1 and not tree[child]:
                tree[child] = node
                dfs(child)

    for _ in range(n - 1):
        first, second = map(int, input().split())

        graph[first].append(second)
        graph[second].append(first)

    dfs(1)

    for node in tree[2:]:
        print(node)


solution(int(input().strip()))
