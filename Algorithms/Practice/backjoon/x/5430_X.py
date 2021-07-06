# https://www.acmicpc.net/board/view/25456
from collections import deque
import sys

input = sys.stdin.readline

# <= 100
tc = int(input())
# 50%에서 실패함 -> [1, 2, 3, 5, 8]이 아니라 [1,2,3,5,8] 로 출력하기를 원함
for _ in range(tc):
    cmds = input()
    size_of_list = int(input())
    _list = input().strip("[]\n ")
    _list = deque([] if len(_list) == 0 else map(int, _list.split(",")))

    is_left = True
    is_error = False
    for cmd in cmds:
        if cmd == "D":
            if len(_list) == 0:
                is_error = True
            elif is_left:
                _list.popleft()
            else:
                _list.pop()
        elif cmd == "R":
            is_left = not is_left
    else:

        if is_error:
            _list = "error"
        else:
            _list = list(_list) if is_left else list(_list)[::-1]

        print(str(_list).replace(" ", ""))

"""
for t in range(tc):
    cmds = input()
    size_of_list = int(input())
    _list = input().strip("[]\n ")
    # map: O(N), size_of_list, 100,000
    # list: O(N), size_of_list
    _list = [] if len(_list) == 0 else list(map(int, _list.split(",")))

    # O(N), cmds, 100,000
    for cmd in cmds:
        if cmd == "D":
            if len(_list) == 0:
                print("error")
                break
            # O(b-a), O(N)
            _list = _list[1:]
        elif cmd == "R":
            _list = _list[::-1]
    else:
        # 파이썬은 초당 20,000,000 가능
        # O(N^2), N, 10,000,000,000
        print(_list)
"""
