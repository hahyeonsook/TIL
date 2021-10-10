from itertools import combinations


def solution(N, M):
    nums = list(map(int, input().strip().split()))

    ans = -1
    for n123 in combinations(nums, 3):
        amount = sum(n123)
        if amount <= M:
            if (M - ans) > (M - amount):
                ans = amount
    return ans


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    print(solution(N, M))
