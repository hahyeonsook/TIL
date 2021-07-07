# 2초 40,000,000 연산 안에 끝내야 함.
# in 연산자는 O(N)
# n <= 100,000 m <= 100,000
# => if m in ns 로 하면 10,000,000,000 넘음.
# 시간초과
import sys

input = sys.stdin.readline
n = int(input().strip())
ns = list(map(int, input().split()))
m = int(input().strip())
ms = list(map(int, input().split()))


def solution(ns, ms):
    """
    def binary_search(lst, target, left=None, right=None):
        left, right = left or 0, right or len(lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if lst[mid] == target:
                return "1"
            elif lst[mid] > target:
                right = mid - 1
            elif lst[mid] < target:
                left = mid + 1
        return "0"
    """

    def binary_search(lst, target, left=None, right=None):
        left, right = left or 0, right or len(lst) - 1
        mid = (left + right) // 2
        if left > right:
            return "0"

        if lst[mid] == target:
            return "1"
        elif lst[mid] > target:
            return binary_search(lst, target, left, mid - 1)
        elif lst[mid] < target:
            return binary_search(lst, target, mid + 1, right)

    ns.sort()
    for m in ms:
        print(binary_search(ns, m))


solution(ns=[4, 1, 5, 2, 3], ms=[1, 3, 7, 9, 5])
