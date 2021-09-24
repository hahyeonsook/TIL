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


# 달팽이

# REF https://www.programmersought.com/article/30524578627/
# 2차원 -> 1차원 달팽이
from pprint import pprint


def snail3(array):
    return list(array[0]) + snail3(list(zip(*array[1:]))[::-1]) if array else []


pprint(snail3([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# 달팽이 채워넣기
# REF https://itzjamie96.github.io/2020/11/18/swea-python-1954/
T = int(input())
#    R, D, L, U
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())
    snail = [[0 for _ in range(N)] for _ in range(N)]

    x, y = 0, -1
    d = 0
    num = 0
    while num < N * N:

        if (
            -1 < x + dx[d % 4] < N  # 이동할 x 값이 -1 보다 크고, N 보다 작을 경우
            and -1 < y + dy[d % 4] < N  # 이동할 y 값이 -1 보다 크고, N 보다 작을 경우
            and snail[x + dx[d % 4]][y + dy[d % 4]] == 0  # 이동할 snail의 값이 초기화된 값일 경우
        ):
            x = x + dx[d % 4]
            y = y + dy[d % 4]
            num += 1
            snail[x][y] = num
        else:
            d += 1
    print(f"#{tc}")
    for x in range(len(snail)):
        print(*snail[x])

# 달팽이 좌표이동
# (n//2, n//2) -> (0, 0)
def snail(n):
    grid = [[-1 for _ in range(n)] for _ in range(n)]
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    d, routine = -1, 0
    r, c = n // 2, n // 2
    while (r, c) != (0, 0):
        d = (d + 1) % 4
        if d % 2 == 0:
            routine += 1

        gr, gc = r + (dr[d] * routine), c + (dc[d] * routine)
        while (r, c) != (gr, gc):
            r, c = r + dr[d], c + dc[d]
            grid[r][c] = 1  # 1 채우기

            if (r, c) == (0, 0):
                break


# 달팽이 좌표이동
# (0, 0) -> (n//2, n//2)
def snail(n):
    grid = [[-1 for _ in range(n)] for _ in range(n)]

    dr, dc = [1, 0, -1, 0], [0, -1, 0, 1]
    d, routine = 2, n
    r, c = 0, -1
    while (r, c) != (n // 2, n // 2):
        d = (d + 1) % 4
        if d % 2 == 0:
            routine -= 1

        gr, gc = r + (dr[d] * routine), c + (dc[d] * routine)
        while (r, c) != (gr, gc):
            r, c = r + dr[d], c + dc[d]
            grid[r][c] = 1  # 1 채우기

            if (r, c) == (n // 2, n // 2):
                break
    return 0


# 여러 줄 입력받기
import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break

# 트라이
import collections


class TrieNode:
    def __init__(self) -> None:
        self.word = False  # 단어가 모두 완성되었을 때, True
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    # 단어 삽입
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        # 단어가 완성되었으므로, 마지막 문자 True
        node.word = True

    # 단어 존재 여부 판별
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        # 마지막에 node.word를 반환하여 해당 문자가 마지막인지 확인함.
        return node.word

    # 문자열로 시작 단어 존재 여부 판별
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        # 마지막 node.word가 True인지 확인하지 않고, 자식 노드가 있는지만 확인함.
        return True


# 진수 변환
# 10진수 -> n진수 변환
digits = "0123456789"


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return digits[r]
    else:
        return convert(q, base) + digits[r]


# 2차원 배열 돌리기
def rotate(matrix) -> None:
    tmp = list(map(list, list(zip(*matrix[::-1]))))
    for i in range(len(tmp)):
        matrix[i] = tmp[i]
