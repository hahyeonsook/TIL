import sys
import collections, heapq

input = sys.stdin.readline


def solution(N):
    graph = collections.defaultdict(list)
    M = int(input().strip())

    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    start_v, end_v = map(int, input().split())
    Q = [(0, start_v)]
    dist = collections.defaultdict(list)

    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    return dist[end_v]


print(solution(int(input().strip())))
