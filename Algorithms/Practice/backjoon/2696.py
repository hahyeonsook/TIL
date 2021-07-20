# REF https://www.acmicpc.net/problem/2696
# 1초, 20,000,000
# 골드 2

import math
import heapq


def solution(t, tcs):
    answer = ""
    for i in range(t):
        median_seq = []
        seq = tcs[i][0]
        seq_lst = map(int, tcs[i][1].split())
        while seq:
            seq = seq % 10
            for num in range(seq):
                if num % 2 != 0:
                    for _ in range(num // 2):
                        heapq.heappop(median_seq)
                    answer += f"{heapq.heappop(median_seq)} "
                    for _ in range(num // 2):
                        heapq.heappush(median_seq, num)


t = 2
tcs = [
    [9, "1 2 3 4 5 6 7 8 9"],
    [9, "9 8 7 6 5 4 3 2 1"],
    [
        23,
        "23 41 13 22 -3 24 -31 -11 -8 -7\n3 5 103 211 -311 -45 -67 -73 -81 -99\n-33 24 56\n",
    ],
]
solution(t, tcs)
