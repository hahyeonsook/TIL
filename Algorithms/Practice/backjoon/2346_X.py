# REF https://www.acmicpc.net/problem/2346
# Silver 3
# 2초, 40,000,000

# N 개의 풍선 안에는 -N <= 종이 <= N 범위의 종이가 들어있음.
# 제일 처음에는 1번 풍선을 터뜨리고, 종이의 수만큼 이동하여 풍선을 터뜨림.
# 양수가 적혀있을 경우, 오른쪽으로 이동하고 음수가 적혀있을 경우, 왼쪽으로 이동함.
# 풍선은 원형으로 놓여있음.
# 이동할 때는 터진 풍선은 빼고 생각함.

# 입력
# 첫 번째 줄에 자연수 N이 주어짐
# 차례로 풍선 안의 주가 적혀짐.
# 1 <= N <= 1,000 (단 0은 제외)

# 출력
# 터진 풍선의 번호를 차례로 나열.

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
ballons = deque(enumerate(map(int, input().split())))
paper = ballons.popleft()
answer = str(paper[0] + 1)

while len(ballons) > 0:
    if paper[1] > 0:
        ballons.rotate(-paper[1])
        paper = ballons.pop()
    else:
        ballons.rotate(-paper[1])
        paper = ballons.popleft()

    answer += f" {paper[0]+1}"

print(answer)


def solution1(n, lst):
    ballons = deque(enumerate(map(int, lst.split())))
    answer = ""
    paper = ballons.popleft()

    while len(ballons) > 0:
        answer += str(paper[0] + 1)

        # rotate(+) = appendleft(q.pop())
        # q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # deque([10, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        # deque([9, 10, 1, 2, 3, 4, 5, 6, 7, 8])
        # deque([8, 9, 10, 1, 2, 3, 4, 5, 6, 7])
        # rotate(-) = append(q.popleft())
        # q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # deque([2, 3, 4, 5, 6, 7, 8, 9, 10, 1])
        # deque([3, 4, 5, 6, 7, 8, 9, 10, 1, 2])
        # deque([4, 5, 6, 7, 8, 9, 10, 1, 2, 3])

        # popleft로 값을 뺄 생각이면 rotate(-) 해야 함.
        # + 일 때, rotate(-)
        # - 일 때, rotate(+)
        # popleft로 값을 뺄 것이기 때문에 rotate(+) 로 넘길때 한 개가 덜 넘어가도록 해야 함.

        if paper[1] > 0:
            ballons.rotate(-(paper[1] - 1))
        else:
            ballons.rotate(-paper[1])

        paper = ballons.popleft()
        answer += " "

    answer += str(paper[0] + 1)

    return answer


def solution2(n, lst):
    ballons = deque(enumerate(map(int, lst.split())))
    paper = ballons.popleft()
    answer = str(paper[0] + 1)

    while len(ballons) > 0:
        if paper[1] > 0:
            # rotate(-) = append(q.popleft())
            ballons.rotate(-paper[1])
            paper = ballons.pop()
        else:
            ballons.rotate(-paper[1])
            paper = ballons.popleft()

        answer += f" {paper[0]+1}"
        print(answer)

    return answer


print("1 4 5 3 2" == solution1(5, "3 2 1 -3 -1"))
print("1 4 5 3 2" == solution2(5, "3 2 1 -3 -1"))


lst = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for i in range(10):
    lst.rotate(1)
    # print(lst)

for i in range(10):
    lst.rotate(-1)
    # print(lst)
