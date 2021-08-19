import sys

input = sys.stdin.readline


def solution(N):
    top = list(map(int, input().split()))
    answer = [0 for _ in range(N)]

    while top:
        i, t = len(top) - 1, top.pop()

        j = i - 1
        while j > -1 and top[j] < t:
            j -= 1

        if j > -1:
            answer[i] = j + 1
    print(*answer)


# 다 실패하고 얘만 성공함..
# https://www.acmicpc.net/board/view/70952 <- 읽어보기
def solution(N):
    top = list(map(int, input().split()))
    answer = [0 for _ in range(N)]
    stack = []

    for i, t in enumerate(top):
        while stack:
            if stack[-1][1] > t:
                answer[i] = stack[-1][0] + 1
                break
            stack.pop()
        stack.append((i, t))

    print(*answer)


solution(int(input().strip()))
