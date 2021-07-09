# 4부 비선형 자료구조/그래프/그래프 순회

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

# 큐를 이용한 반복 구조로 구현
def iterative_bfs(start_v):
    discovered = [start_v]
    # queue는 검사해야 할 노드의 목록
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

# 백트래킹
# 백트래킹은 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되면, 즉시 후보를 포기(Backtrack)하고 정답을 찾아가는 범용적인 알고리즘
# 탐색을 하다가 더 갈 수 없으면 왔더 길을 되돌아가 다른 길을 찾는다는 데서 유래했다. DFS는 백트래킹의 골격을 이루는 알고리즘이다.
# 주로 재귀로 구현하며, 기본적으로 모두 DFS의 범주에 속한다.

# 섬의 개수
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]


def numIsIsland(grid: list[list[str]]) -> int:
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return

        grid[i][j] = "0"

        # 동서남북 탐색
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(i, j)
                # 모든 육지 탐색 후 카운트 1 증가
                count += 1
    return count


print(f"numIsIsland: {numIsIsland(grid1)}")  # 1
print(f"numIsIsland: {numIsIsland(grid2)}")  # 3


# 전화번호 문자 조합
# 2에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자를 출력하라.

# 모든 조합 탐색
def letterCombinations(digits: str) -> list[str]:
    def dfs(index, path):
        # 끝까지 탐색하면 백트래킹
        if len(path) == len(digits):
            result.append(path)
            return

        # 입력값 자릿수 단위 반복
        # digits에서 이미 탐색한 값은 다시 탐색하지 않기 위해 index를 넣음.
        for i in range(index, len(digits)):
            # 숫자에 해당하는 모든 문자열 반복
            for j in dic[digits[i]]:
                dfs(i + 1, path + j)

    if not digits:
        return []

    dic = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    result = []
    dfs(0, "")

    return result


# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print(f"letterCombination: {letterCombinations('23')}")


# 순열
# 서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라.
nums = [1, 2, 3]


def permute(nums: list[int]) -> list[list[int]]:
    results = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])

        # 순열 생성 재귀 호출
        for e in elements:
            # 참조가 아니라 값을 복사
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results


# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(f"permute: {permute(nums)}")


# itertools 모듈 사용
import itertools


def permute(nums: list[int]) -> list[list[int]]:
    # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    # return list(itertools.permutations(nums))
    return list(map(list, itertools.permutations(nums)))


# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(f"permute: {permute(nums)}")


# 조합
# 전체 수 n을 입력받아 k개의 조합을 리턴하라.
n = 4
k = 2


def combine(n: int, k: int) -> list[list[int]]:
    results = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            return

        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return results


print(f"combine: {combine(n, k)}")


def combine(n: int, k: int) -> list[list[int]]:
    return list(itertools.combinations(range(1, n + 1), k))
