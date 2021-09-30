"""
# 764ms
import sys

input = sys.stdin.readline
A = " " + input().strip()
B = " " + input().strip()

C, R = len(A), len(B)
dp = [["" for _ in range(C)] for _ in range(R)]
for r in range(1, R):
    for c in range(1, C):
        if A[c] == B[r]:
            dp[r][c] = dp[r - 1][c - 1] + B[r]
        else:
            if len(dp[r - 1][c]) < len(dp[r][c - 1]):
                dp[r][c] = dp[r][c - 1]
            else:
                dp[r][c] = dp[r - 1][c]

ans = dp[-1][-1]
print(len(ans))
print(ans)
"""
"""
# https://www.acmicpc.net/source/33403656 참고
# 700ms
import sys

input = sys.stdin.readline
A = " " + input().strip()
B = " " + input().strip()

C, R = len(A), len(B)
dp = [[0 for _ in range(C)] for _ in range(R)]
for r in range(1, R):
    for c in range(1, C):
        if A[c] == B[r]:
            dp[r][c] = dp[r - 1][c - 1] + 1
        else:
            dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

print(dp[-1][-1])

ans = ""
r, c = R - 1, C - 1
while r > 0 and c > 0:
    if A[c] == B[r]:
        ans += A[c]
        r -= 1
        c -= 1
    elif dp[r - 1][c] > dp[r][c - 1]:
        r -= 1
    else:
        c -= 1
print(ans[::-1])
"""

"""
# 588ms
import sys


def solution(A, B):
    C, R = len(A), len(B)
    dp = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(1, R):
        for c in range(1, C):
            if A[c] == B[r]:
                dp[r][c] = dp[r - 1][c - 1] + 1
            else:
                dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

    ans = ""
    r, c = R - 1, C - 1
    while r > 0 and c > 0:
        if A[c] == B[r]:
            ans += A[c]
            r -= 1
            c -= 1
        elif dp[r - 1][c] > dp[r][c - 1]:
            r -= 1
        else:
            c -= 1

    print(dp[-1][-1])
    print(ans[::-1])


if __name__ == "__main__":

    input = sys.stdin.readline
    A = " " + input().strip()
    B = " " + input().strip()
    solution(A, B)
"""

# 516ms
import sys


def solution(A, B):
    C, R = len(A), len(B)
    dp = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(1, R):
        for c in range(1, C):
            if A[c] == B[r]:
                dp[r][c] = dp[r - 1][c - 1] + 1
            else:
                dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

    ans = ""
    r, c = R - 1, C - 1
    while r > 0 and c > 0:
        if A[c] == B[r]:
            ans = A[c] + ans
            r -= 1
            c -= 1
        elif dp[r - 1][c] > dp[r][c - 1]:
            r -= 1
        else:
            c -= 1

    print(dp[-1][-1])
    print(ans)


if __name__ == "__main__":

    input = sys.stdin.readline
    A = " " + input().strip()
    B = " " + input().strip()
    solution(A, B)
