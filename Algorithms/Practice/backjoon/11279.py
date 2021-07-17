# REF https://www.acmicpc.net/problem/11279
# 1초, 20,000,000
# 실버 3

# 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하라.
# 1. 배열에 자연수 x를 넣는다.
# 2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.

# 입력
# N, 연산의 개수, 1 <= N <= 100,000
# N개의 줄, 연산에 대한 정보를 나타내는 정수 x,
#          x == 자연수, 1번 연산
#          x == 0, 2번 연산

# 출력
# 0이 주어진 회수만큼 답을 출력하라.
# 빈 배열일 경우, 0을 출력하라.

import sys, heapq

input = sys.stdin.readline
n = int(input().strip())


def solution(n):
    lst = []
    results = []
    for _ in range(n):
        x = int(input().strip())

        if x == 0:
            if len(lst) == 0:
                results.append(0)
            else:
                results.append(heapq.heappop(lst) * -1)
        else:
            heapq.heappush(lst, -x)
    return results


print("\n".join(map(str, solution(n))))
