import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def solution(M, N):
    maps = []
    for _ in range(M):
        maps.append(list(map(int, input().split())))

    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    visited = [[-1 for _ in range(N)] for _ in range(M)]
    visited[0][0] = 1

    def dfs(r, c):
        if visited[r][c] != -1:
            return visited[r][c]

        visited[r][c] = 0
        for mr, mc in zip(dr, dc):
            wr, wc = r + mr, c + mc
            if 0 <= wr < M and 0 <= wc < N and maps[r][c] < maps[wr][wc]:
                visited[r][c] += dfs(wr, wc)
        return visited[r][c]

    return dfs(M - 1, N - 1)


M, N = map(int, input().split())
print(solution(M, N))
