import sys
import collections, heapq

input = sys.stdin.readline


def solution(V, E):
    K = int(input().strip())
    graph = collections.defaultdict(list)

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    Q = [(0, K)]
    dist = collections.defaultdict(int)
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for u, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, u))

    for node in range(1, V + 1):
        if not dist[node] and node != K:
            print("INF")
        else:
            print(dist[node])


V, E = map(int, input().split())
solution(V, E)
