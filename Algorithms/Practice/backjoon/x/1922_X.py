# REF https://www.acmicpc.net/problem/1922
# 2초, 40,000,000
# 골드 4

# 컴퓨터와 컴퓨터를 연결하는 네트워크를 구축하려 한다.
# 허브가 없기 때문에 컴퓨터끼리 직접 연결해야 한다.
# A-B, B-C 이면 A-C이다.
# 최소 연결 비용을 출력하라.

# 입력
# 컴퓨터 수, 1<= n <= 1000
# 연결할 수 있는 선의 수, 1 <= m <= 100,000
# 각 컴퓨터를 연결하는데 드는 비용, a b c, a-b 연결 비용은 c

# 출력
# 최소비용


import collections


def solution(n, m, costs):
    graph = collections.defaultdict(list)
    for cost in costs:
        first_node, second_node, edge_cost = map(int, cost.split())
        graph[first_node].append((second_node, edge_cost))
        graph[second_node].append((first_node, edge_cost))
    min_cost = 0

    def dfs(start_v, sum=0, discovered=[]):
        discovered.append(start_v)
        for w in graph[start_v]:
            if w[0] not in discovered:
                discovered, sum = dfs(w[0], sum + w[1], discovered)
        return discovered, sum

    print(dfs(1))


lst = [
    "1 2 5",
    "1 3 4",
    "2 3 2",
    "2 4 7",
    "3 4 6",
    "3 5 11",
    "4 5 3",
    "4 6 8",
    "5 6 8",
]
solution(6, 9, lst)
