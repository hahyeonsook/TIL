# REF https://www.acmicpc.net/problem/7662
# 6초, 120,000,000
# 골드 5

# 이중 우선순위 큐는 데이터를 삭제할 때, 연산에 따라 우선순위가 가장 높은 데이터 또는 가장 낮은 데이터 중 하나를 삭제한다.
# 연산 종류
# 1. 데이터 삽입
# 2. 데이터 삭제
# 2-1. 우선순위가 가장 높은 것을 삭제
# 2-2. 우선순위가 가장 낮은 것을 삭제
# 연산이 주어질 때, 연산을 처리하고 남은 데이터 중 최댓값과 최솟값을 출력하가.

# 입력
# T, 테스트 데이터,
# k, Q에 적용할 연산의 개수, k <= 1,000,000
# k개의 줄, 연산 문자(D or I)
#           D 1, 최댓값 삭제
#           D -1, 최솟값 삭제
#           비었는데, D일 경우 무시한다.
#           I n, 정수 n을 Q에 삽입

# heapq 모듈은 최솟값은 인덱스 0으로 보장되지만, 그 이후의 값에 대해서는 인덱스로 보장하지 않음.

from heapq import heappush
from io import StringIO
import sys

input = sys.stdin.readline
# t = int(input().strip())
string = [
    "I 16",
    "I -5643",
    "D -1",
    "D 1",
    "D 1",
    "I 123",
    "D -1",
]


def solution(t):
    import heapq

    results = []

    for _ in range(t):
        Q = {}
        min_Q = []
        max_Q = []
        # k = int(input().strip())
        k = 7
        for i in range(k):
            op, num = string[i].split()
            if op == "I":
                heapq.heappush(min_Q, int(num))
                heapq.heappush(max_Q, -int(num))
            if op == "D" and Q:
                if int(num) > 0:
                    heapq.heappop(max_Q)
                else:
                    heapq.heappop(min_Q)

            mid = len(min_Q) // 2
            Q = min_Q[:mid] + max_Q[mid:]
            min_Q, max_Q = Q[:], Q[:]
        if Q:
            results.append(f"{max(Q)} {min(Q)}")
        else:
            results.append("EMPTY")
    return results


print("\n".join(map(str, solution(1))))
