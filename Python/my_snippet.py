import re

s = "Hello World!"
# 숫자와 문자가 아닌 것 제거
print(re.sub("[^A-Za-z0-9]", "", s))
# 단어 문자가 아닌 것 제거
print(re.sub("[^\w]", "", s))

# 스택
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
stack = []  # height의 인덱스를 넣음
for i in range(len(height)):
    while stack and height[i] > height[stack[-1]]:
        top = stack.pop()

        if not len(stack):
            break

    stack.append(i)

# 짝수번째 더하기
nums = [1, 4, 3, 2]
print(sum(sorted(nums)[::2]))


# DFS

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

# 재귀로 표현
def recursive_dfs(v: int, discovered=[]) -> list[int]:
    discovered.append(v)
    # 자식 노드가 없는 4, 6의 경우 for 문으로 들어가지 않고 return 하도록 함.
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered


print(recursive_dfs(1))  # [1, 2, 5, 6, 7, 3, 4]

# 스택을 이용한 반복 구조로 구현
def iterative_dfs(start_v: int) -> list[int]:
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        # 루프 문이 시작되기 전에 확인했다고 표시했으므로,
        # 루프 문에서 볼 자식 노드의 부모 노드만 확인했다고 표시한 것.
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered


print(iterative_dfs(1))  # [1, 4, 3, 5, 7, 6, 2]


# BFS
# BFS는 재귀로 동작하지 않는다.
# 큐를 이용한 반복 구조로 구현.
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        # v의 모든 자식 노드를 순회
        for w in graph[v]:
            # 루프 문이 시작되고 자식 노드를 queue에 넣을 때 확인했음을 표시했으므로,
            # 한 부모 노드의 모든 자식 노드를 확인했다고 표시한 것.
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered


print(iterative_bfs(1))  # [1, 2, 3, 4, 5, 6, 7]

# 이진 탐색 with loop
# 찾으면 index, 못찾으면 -1을 리턴
def binary_search(lst, target, left=None, right=None):
    left, right = left or 0, right or len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            right = mid - 1
        elif lst[mid] < target:
            left = mid + 1
    return -1


# 이진 탐색 with recursive
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


# 최대공약수
from functools import reduce
from math import gcd as _gcd


def gcd(numbers):
    return reduce(_gcd, numbers)


# 최대공약수
# 유클리드 알고리즘

# 1. a, b(a > b)
# 2. b == 0, return a
# 3. a % b != 0, a = b b = a % b, 1로 다시 돌아감
# 4. a % b == 0, return b


def _gcd(a, b):
    a, b = a, b if a > b else b, a
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


# 문자열이 아닌 리스트 join으로 출력하기
lst = [1, 2, 3, 4]
print(" ".join(map(str, lst)))


# 조합 Combination
# nCm, 순서를 고려하지 않고 n 개중에서 m개를 늘어놓음.
# nCm = nPm/m! = n!/r!(n-r)!
# https://juhee-maeng.tistory.com/91
from itertools import combinations

for i in combinations([1, 2, 3, 4], 2):
    print(i, end=" ")

# 조합
# https://m.blog.naver.com/PostView.nhn?blogId=kmh03214&logNo=221685090465&targetKeyword=&targetRecommendationCode=1
def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[1]]
        for next in combinations(arr[i + 1], r - 1):
            yield [arr[i] + next]


# 소수 구하기
import math


def isPrime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
