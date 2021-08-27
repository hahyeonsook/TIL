import sys

input = sys.stdin.readline


def solution(T):
    ans = []
    A = 60 * 5
    B = 60
    C = 10

    ans.append(T // A)
    T = T % A

    ans.append(T // B)
    T = T % B

    ans.append(T // C)
    T = T % C

    if T != 0:
        return [-1]

    return ans


print(*solution(int(input().strip())))
