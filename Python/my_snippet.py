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
