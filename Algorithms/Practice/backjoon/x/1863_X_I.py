# 건물들의 윤곽을 스카이라인이라고 한다.
# 건물은 모두 직사각형 모양이다.
# 스카이라인을 보고 건물이 최소한 몇 채인지 알아내라.

# 최소 1개는 존재해야 하는 건물이 최대한 넓은 범위를 커버해야 최소의 개수를 찾을 수 있다.

# 입력
# * n , n개의 고도가 바뀌는 지점, 1 <= n <= 50,000
# * x y , 고도가 바뀌는 지점의 좌표 x y, 1 <= x <= 1,000,000 0 <= y <=500,000

# 출력
# 최소 건물의 개수

# 48%에서 틀림
# 다시 구상해봤는데, 코드 구현이 틀림.
"""
import sys

input = sys.stdin.readline

n = int(input())

cnt = 0
stack = []

for _ in range(n):
    x, y = map(int, input().split())

    while len(stack) != 0 and stack[-1] > y:
        stack.pop()
        cnt += 1
    if len(stack) != 0 and stack[-1] == y:
        continue
    stack.append(y)

while len(stack) != 0 and stack[-1] > y:
    stack.pop()
    cnt += 1
print(cnt)

"""


def solution(lst):
    n = int(lst[0])
    cnt = 0
    stack = []

    for line in lst[1:]:
        x, y = map(int, line.split())

        while len(stack) != 0 and stack[-1] > y:
            stack.pop()
            cnt += 1
        if len(stack) != 0 and stack[-1] == y:
            continue
        stack.append(y)

    while len(stack) > 0:
        stack.pop()
        cnt += 1

    print(cnt)


solution(
    [
        "10",
        "1 1",
        "2 2",
        "5 1",
        "6 3",
        "8 1",
        "11 0",
        "15 2",
        "17 3",
        "20 2",
        "22 1",
    ]
)
