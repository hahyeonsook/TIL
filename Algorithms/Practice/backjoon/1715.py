import sys, heapq

input = sys.stdin.readline


def solution(N):
    heap = []
    for _ in range(N):
        heapq.heappush(heap, int(input().strip()))

    ans = 0
    while len(heap) > 1:
        op1 = heapq.heappop(heap)
        op2 = heapq.heappop(heap)
        ans += op1 + op2
        heapq.heappush(heap, op1 + op2)
    return ans


print(solution(int(input().strip())))
