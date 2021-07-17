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
from typing import List


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


import collections


def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []

    def dfs(a):
        # 첫 번째 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs("JFK")
    # 다시 뒤집어 어휘 순 결과로
    return route[::-1]


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(findItinerary(tickets))


def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    # reverse 한 것은 pop 할때, pop(0)이 아닌 pop()으로 쓰기 위해서임
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []

    def dfs(a):
        # 마지막 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs("JFK")
    # 다시 뒤집어 어휘 순 결과로
    return route[::-1]


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(findItinerary(tickets))


def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)

    route, stack = [], ["JFK"]

    while stack:
        # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    return route[::-1]


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(findItinerary(tickets))


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        # 탐색 종료 후 순환 노드 삭제

        return True

    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False
    return True


# 한 번 방문했던 그래프는 두 번 이상 방문하지 않도록 무조건 True로 리턴


def canFinish(numCourses: int, prerequisties: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisties:
        graph[x].append(y)

    traced = set()
    visited = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False
        # 이미 방문했던 노드이면 False
        if i in visited:
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True


# K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라.
# N은 전체 노드의 개수
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2


import heapq


def networkDelayTime(times: List[List[int]], N: int, K: int) -> int:
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in times:
        graph[u].append((v, w))

    # 큐 변수: [(소요 시간, 정점)]
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        # 노드가 dist에 없을 경우에만 힙에 푸시함.
        # 최소 힙에 의해 해당 노드에서 제일 처음에 나오는 값은 최솟값일 것이므로
        # dist에 항상 최솟값만 세팅될 수 있음.
        # dist는 (노드, 노드까지 걸리는 시간)을 나타냄.
        if node not in dist:
            # dist에 존재하면, 값을 버림.
            # dist에는 항상 최솟값부터 세팅되기 때문에
            # 이미 값이 존재한다면 그 값은 이미 최단 경로이고,
            # 새롭게 큐에 삽입되는 값은 더 오래 걸리는 경로이므로 이 값은 버린다.
            dist[node] = time
            # 도착지, 소요 시간
            # node, K의 간선들을 loop 함.
            # K에서 v까지 소요되는 시간에 K까지 오는데 걸리는 시간을 더해서 Q에 저장함.
            for v, w in graph[node]:
                alt = time + w
                # 소요 시간, 정점
                heapq.heappush(Q, (alt, v))

    # 모든 노드의 최단 경로 존재 여부 판별
    # len(dist) == N 이면 모든 노드의 최단 경로를 구했다는 의미이고,
    # 이는 모두 시작점에서 도달이 가능하다는 의미이다.
    # dist에 노드가 없다면, 그 노드는 시작점에서 도달할 수 없다는 뜻이며, -1을 리턴한다.
    if len(dist) == N:
        return max(dist.values())
    return -1


print(networkDelayTime(times, N, K))

times = [
    [3, 1, 5],
    [3, 2, 2],
    [2, 1, 2],
    [3, 4, 1],
    [4, 5, 1],
    [5, 6, 1],
    [6, 7, 1],
    [7, 8, 1],
    [8, 1, 1],
]
N = 8
K = 3

print(networkDelayTime(times, N, K))

n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
# 시작점
src = 0
# 도착점
dst = 2
# 경유지 개수
K = 0


def findCheapsPrice(
    n: int, flights: List[List[int]], src: int, dst: int, K: int
) -> int:
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in flights:
        graph[u].append((v, w))

    # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
    Q = [(0, src, K)]

    # 우선순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        # k를 넘어서는 경로는 더 이상 탐색되지 않도록 추가함.
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush((alt, v, k - 1))
    return -1


# 그래프와 트리
# 트리는 순환 구조를 갖지 않는 그래프이다.
# 트리는 특수한 형태의 그래프의 일종이나 어떠한 경우에도 한번 연결된 노드가 다시 연결되는 법이 없다.
# 단방향, 양방향 모두 가리킬 수 있는 그래프와 달리, 부모에서 자식을 가리키는 단방향뿐이다.
# 또한 트리는 하나의 부모 노드를 갖는다. 루트 또한 하나여야 한다.

# 이진 트리
# 각 노드가 m개 이하의 자식을 갖고 있으면, m-ary 트리라고 한다. m=2일 경우,
# 모든 노드의 차수가 2 이하일 때는 특별이 이진 트리라고 구분해서 부른다.
# 여러 알고리즘을 구현한느 일도 좀 더 간단하게 처리할 수 있고, 다진 트리에 비해 훨씬 간결해서 많이 쓰인다.

# 정이진트리: 모든 노드가 0개 또는 2개의 자식 노드를 갖는다.
# 완전이진트리: 마지막 레벨을 제외하고 모든 레벨이 완전히 채워져 있으며, 마지막 레벨의 모든 노드는 가장 왼쪽부터 채워져 있다.
# 포화이진트리: 모든 노드가 2개의 자식 노드를 갖고 있으며, 모든 리프 노드가 동일한 깊이 또는 레벨을 갖는다.

# 이진 트리의 최대 깊이를 구하라.
