import sys

input = sys.stdin.readline


def solution(N, M):
    cnt = 0
    arr = list(map(int, input().split()))

    m = arr[0]
    cnt, left, right = 0, 0, 0
    while right < N - 1:
        if m < M:
            right += 1
            m += arr[right]
        elif m > M:
            m -= arr[left]

            left += 1
            m += arr[left]
        else:
            cnt += 1
            left += 1
            right += 1

    return cnt


N, M = map(int, input().split())
print(solution(N, M))

"""
1 1
1
"""

"""
6 13

2 3 5 7 11 13
"""
