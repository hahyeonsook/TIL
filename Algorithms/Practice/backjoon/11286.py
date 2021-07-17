# REF https://www.acmicpc.net/problem/11286
# 1초, 20,000,000
# 실버 1

# 절댓값 힙은 다음과 같은 연산을 지원한다.
# 배열에 정수 x (x ≠ 0)를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.

import sys

input = sys.stdin.readline

n = int(input().strip())


def solution(n):
    import heapq

    lst = []
    results = []
    for _ in range(n):
        x = int(input().strip())

        abs = x if x > 0 else x * -1
        val = x

        if x == 0:
            if len(lst) == 0:
                results.append(0)
            else:
                results.append(heapq.heappop(lst)[1])
        else:
            heapq.heappush(lst, (abs, val))
    return results


print("\n".join(map(str, solution(n))))
