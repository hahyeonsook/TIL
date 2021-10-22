def dfs(r, c, cnt):
    global answer
    if cnt > answer:
        answer = cnt
    for d in range(4):
        mr, mc = r + dr[d], c + dc[d]
        if -1 < mr < R and -1 < mc < C and not visited[mr][mc]:
            if not alphabets[maps[mr][mc]]:
                visited[mr][mc] = True
                alphabets[maps[mr][mc]] = True
                dfs(mr, mc, cnt + 1)
                visited[mr][mc] = False
                alphabets[maps[mr][mc]] = False
    return

if __name__ == "__main__":
    R, C = map(int, input().split())
    alphabets = [False] * 26
    maps = [[ord(char) - 65 for char in input().strip()] for _ in range(R)]
    visited = [[False for _ in range(C)] for _ in range(R)]

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    answer = -1
    visited[0][0] = True
    alphabets[maps[0][0]] = True
    dfs(0, 0, 1)
    print(answer)
