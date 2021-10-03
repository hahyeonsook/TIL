# 브루투포스
# 29200kb 112ms -> 29200kb 108ms
def solution(N, M):
    board = [list(input().strip()) for _ in range(N)]
    chessspace = {1: "B", -1: "W"}

    def check(sr, sc):
        amt = []
        er, ec = sr + 8, sc + 8
        for space in [1, -1]:
            cnt = 0
            for r in range(sr, er):
                for c in range(sc, ec):
                    if board[r][c] != chessspace[space]:
                        cnt += 1
                    space *= -1
                space *= -1
            amt.append(cnt)
        return min(amt)

    cnt = int(1e9)
    N, M = N - 7, M - 7
    for r in range(N):
        for c in range(M):
            cnt = min(cnt, check(r, c))

    return cnt


# 29200kb 100ms
# 매번 min으로 값을 비교하는 것보다 값을 모두 list에 넣은 후, 한번에 min으로 비교하는게 더 빠름.
def solution(N, M):
    board = [input().strip() for _ in range(N)]

    def check(sr, sc):
        amt = []
        chessboard = ["WBWBWBWB", "BWBWBWBW"]
        er, ec = sr + 8, sc + 8
        for chess in chessboard:
            cnt = 0
            for r in range(sr, er):
                for char1, char2 in zip(board[r][sc:ec], chess):
                    if char1 != char2:
                        cnt += 1
                chess = chess[::-1]
            amt.append(cnt)
        return min(amt)

    cnt = []
    N, M = N - 7, M - 7
    for r in range(N):
        for c in range(M):
            cnt.append(check(r, c))

    return min(cnt)


# 비트마스크 & 브루투포스
# 31924kb 176ms
from collections import Counter


def solution(N, M):
    board = [list(input().strip()) for _ in range(N)]

    # str -> binary 변환
    for r in range(N):
        column = ""
        for c in range(M):
            if board[r][c] == "W":
                column += "1"
            else:
                column += "0"
        board[r] = column

    def mask(sr, sc):
        chessboard = ["10101010", "01010101"]

        amt = 65
        er, ec = sr + 8, sc + 8
        for chess in chessboard:
            cnt = 0
            for r in range(sr, er):
                cnt += Counter(bin(int(chess, 2) ^ int(board[r][sc:ec], 2)))["1"]
                chess = chess[::-1]
            amt = min(amt, cnt)
        return amt

    min_cnt = int(1e9)
    N, M = N - 7, M - 7
    for r in range(N):
        for c in range(M):
            min_cnt = min(min_cnt, mask(r, c))

    return min_cnt


# dp, 브루투포스
# https://www.acmicpc.net/board/view/62925

if __name__ == "__main__":
    N, M = map(int, input().split())
    print(solution(N, M))
