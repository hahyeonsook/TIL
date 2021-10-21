# bfs + bineary_search
import sys
from collections import deque

input = sys.stdin.readline

max_w = -sys.maxsize
N, M = map(int, input().split())
bridges = [list() for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    bridges[u].append((v, w))
    bridges[v].append((u, w))
    max_w = max(max_w, w)

S, E = map(int, input().split())


def bfs(weight):
    visited = [False] * (N + 1)
    visited[S] = True
    queue = deque([S])

    while queue:
        v = queue.popleft()
        if v == E:
            return True
        for u, w in bridges[v]:
            if not visited[u] and w >= weight:
                visited[u] = True
                queue.append(u)
    return False


def bineary_search(lo, hi):
    while lo <= hi:
        mid = (lo + hi) // 2
        if bfs(mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return hi


print(bineary_search(1, max_w))

# dfs + memoization으로 풀수 있다고 함.
