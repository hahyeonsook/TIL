import sys

input = sys.stdin.readline

ASCII = 65
R, C = map(int, input().split())
dist = [[-1 for _ in range(C)] for _ in range(R)]
dist[0][0] = 1
maps = []

for _ in range(R):
    maps.append(input().strip())

cnt = -1
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]


def dfs(dist, vr, vc, visited, alphabets):
    alphabet = ord(maps[vr][vc]) - ASCII

    alphabets[alphabet], visited[vr][vc] = True, True
    for d in range(4):
        wr, wc = vr + dr[d], vc + dc[d]
        if -1 < wr < R and -1 < wc < C and not visited[wr][wc]:
            visited, alphabets = dfs(dist + 1, wr, wc, visited, alphabets)

    alphabets[alphabet], visited[vr][vc] = False, False
    return visited, alphabets


alphabets = [False] * 26
visited = [[False for _ in range(C)] for _ in range(R)]
print(dfs(1, 0, 0, visited, alphabets))
