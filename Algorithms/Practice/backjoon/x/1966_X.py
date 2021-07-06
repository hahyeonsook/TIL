# REF https://www.acmicpc.net/problem/1966
# Sliver 3
# 2초, 40,000,000

# 현재 Queue의 가장 앞에 있는 문서의 중요도를 확인한다.
# 현재 Queue에서 중요도가 가장 높다면 인쇄한다.
# 나머지 문서들 중 가장 앞의 문서보다 중요도가 높은 문서가 있으면, Queue의 가장 뒤에 배치한다.
# Queue의 문서의 수와 중요도가 주어질 때, 임의의 문서가 몇 번째로 인쇄되는지 알아내라.

# 입력
# 첫번 째 줄, test case 수
# tc의 첫번 째 줄, 문서의 개수, 1 <= n <= 100, 임의의 문서의 위치, 0 <= m <=n
# tc의 두번 째 줄, n개의 문서의 중요도, 1 <= <= 9, 중요도는 중복될 수 있다.

# 출력
# 각 tc에 대해 문서가 몇 번째로 인쇄되는지 출력하라.

# 시간초과

import sys
from collections import deque
from string import ascii_uppercase


input = sys.stdin.readline
"""
tc = int(input().strip())

for _ in range(tc):
    cnt = 0
    n, m = map(int, input().split())

    docs_list = list(ascii_uppercase)[:n]
    doc = docs_list[m]

    _list = list(map(int, input().split()))

    sorted_list = deque(sorted(_list, reverse=True))

    docs_list = deque(zip(docs_list, _list))

    while len(docs_list) != 0:
        front = docs_list.popleft()
        if front[0] == doc and front[1] == sorted_list[0]:
            cnt += 1
            break

        if front[1] == sorted_list[0]:
            sorted_list.popleft()
            cnt += 1
        else:
            docs_list.append(front)

    print(cnt)
"""


def solution(tcs, sol):
    cnt = 0
    n, m = map(int, tcs[0].split())
    docs_name = deque(list(ascii_uppercase)[:n])
    doc = docs_name[m]

    _list = deque(map(int, tcs[1].split()))
    sorted_list = deque(sorted(_list, reverse=True))
    docs_list = deque(zip(docs_name, _list))
    print(docs_list)
    while len(docs_list) != 0:
        front = docs_list.popleft()
        if front[0] == doc and front[1] == sorted_list[0]:
            cnt += 1
            break
        if front[1] == sorted_list[0]:
            sorted_list.popleft()
            cnt += 1
        else:
            docs_list.append(front)
    print(sol == cnt)


solution(["1 0", "5"], 1)
solution(["4 2", "1 2 3 4"], 2)
solution(["6 0", "1 1 9 1 1 1"], 5)
