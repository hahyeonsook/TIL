# REF https://www.acmicpc.net/problem/1260
# 2초, 40,000,000

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하라.
# 번호가 작은 것부터 탐색하고, 더 이상 방문할 수 있는 점이 없을 경우 종료.
# 정점의 개수 n, 1 <= n <= 1,000
# 간선의 개수 m, 1 <= m <= 10,000
# 탐색을 시작할 정점의 번호 v
# 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 입력
# n m v
# m개 줄의 간선이 연결하는 두 정점의 번호

# 출력
# 첫째 줄, DFS 결과
# 둘째 줄, BFS 결과


def backjoon():
    import sys

    input = sys.stdin.readline
    n, m, start_v = map(int, input().split())
    graph = {i + 1: [] for i in range(n)}
    for _ in range(m):
        first_node, second_node = map(int, input().split())
        graph[first_node].append(second_node)
        graph[second_node].append(first_node)

    def dfs(start_v):
        discovered = []
        stack = [start_v]
        while stack:
            v = stack.pop()
            if v not in discovered:
                discovered.append(v)
                for w in sorted(graph[v], reverse=True):
                    stack.append(w)
        return discovered

    def bfs(start_v):
        discovered = [start_v]
        queue = [start_v]
        while queue:
            v = queue.pop(0)
            for w in sorted(graph[v]):
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)
        return discovered

    print(" ".join(map(str, dfs(start_v))))
    print(" ".join(map(str, bfs(start_v))))


def solution(n, m, start_v, edges):
    graph = {i + 1: [] for i in range(n)}
    for edge in edges:
        first_node, second_node = map(int, edge.split())
        graph[first_node].append(second_node)
        graph[second_node].append(first_node)

    def dfs(start_v):
        discovered = []
        stack = [start_v]
        while stack:
            v = stack.pop()
            if v not in discovered:
                discovered.append(v)
                for w in sorted(graph[v], reverse=True):
                    stack.append(w)
        return discovered

    def bfs(start_v):
        discovered = [start_v]
        queue = [start_v]
        while queue:
            v = queue.pop(0)
            for w in sorted(graph[v]):
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)
        return discovered

    print(" ".join(map(str, dfs(start_v))))
    print(" ".join(map(str, bfs(start_v))))


edges1 = [
    "1 2",
    "1 3",
    "1 4",
    "2 4",
    "3 4",
]
edges2 = [
    "5 4",
    "5 2",
    "1 2",
    "3 4",
    "3 1",
]
edges3 = ["999 1000"]
# solution(4, 5, 1, edges1)
# solution(5, 5, 3, edges2)
# solution(1000, 1, 1000, edges3)
backjoon()
