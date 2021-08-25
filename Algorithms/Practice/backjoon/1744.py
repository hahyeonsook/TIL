import sys

input = sys.stdin.readline


def solution(N):
    arr = []
    one, zero = 0, 0
    for _ in range(N):
        arr.append(int(input().strip()))
        if arr[-1] <= 0:
            zero += 1
        elif arr[-1] == 1:
            one += 1
    arr.sort()

    ans = []
    positive = sorted(arr[zero:])[one:]
    while len(positive) > 1:
        ans.append(positive.pop() * positive.pop())
    ans += positive

    negative = sorted(arr[:zero], reverse=True)
    while len(negative) > 1:
        ans.append(negative.pop() * negative.pop())
    ans += negative

    return sum(ans) + one


print(solution(int(input().strip())))
