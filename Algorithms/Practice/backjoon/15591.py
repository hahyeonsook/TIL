from collections import deque

# 시간초과
def solution(N, Q):
    dp = [[int(1e9) for _ in range(N)] for _ in range(N)]

    for n in range(N):
        dp[n][n] = 0

    for _ in range(N - 1):
        p, q, r = map(int, input().split())
        dp[p - 1][q - 1] = dp[q - 1][p - 1] = r

    def bfs(start, end):
        visited = [False] * N

        visited[start] = True
        queue = deque([start])

        while queue:
            v = queue.popleft()
            for u, w in enumerate(dp[v]):
                if end == u:
                    return
                if not visited[u] and 0 < w < int(1e9):
                    queue.append(u)
                    visited[u] = True

                    if dp[start][end] > w:
                        dp[start][end] = w
        return

    count = []
    for _ in range(Q):
        k, v = map(int, input().split())
        for u in range(N):
            if dp[v - 1][u] == int(1e9):
                bfs(v, u)
                dp[u][v] = dp[v][u]
        count.append(str(len(list(filter(lambda u: u >= k, dp[v - 1])))))

    return "\n".join(count)


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
