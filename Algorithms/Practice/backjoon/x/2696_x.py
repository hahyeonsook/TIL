# REF https://www.acmicpc.net/problem/2696
# 1초, 20,000,000
# 골드 2

# 입력
# t, 테스트 케이스, 1<=t<=1,000
# m, 수열의 크기, 1<=m<=9999

# 50% 시간초과
# https://derekahndev.github.io/problem%20solving/boj-2696/

import sys

input = sys.stdin.readline

import heapq


def solution2(t):
    for _ in range(t):  # O(t)
        m = int(input().strip())
        m_seq = []

        seq = []
        c_seq = []

        for _ in range(0, m, 10):  # O(m/10)
            seq += list(map(int, input().split()))

        for last in range(0, len(seq), 2):  # O(m/2)
            tmp = []
            start = len(c_seq)
            # O(log2)
            list(map(lambda x: heapq.heappush(c_seq, x), seq[start : last + 1]))
            # O(log(len(c_seq)/2))
            for _ in range(len(c_seq) // 2):
                heapq.heappush(tmp, heapq.heappop(c_seq))

            c_median = heapq.heappop(c_seq)
            m_seq.append(c_median)
            heapq.heappush(c_seq, c_median)
            # O(log(len(c_seq)/2))
            while tmp:
                heapq.heappush(c_seq, tmp.pop())

        sys.stdout.write(str(len(m_seq)) + "\n")
        while m_seq:
            sys.stdout.write(" ".join(map(str, m_seq[:10])) + "\n")
            m_seq = m_seq[10:]


def solution(t):
    for _ in range(t):
        m = int(input().strip())
        t_seq = []
        m_seq = []

        for mul in range(0, m, 10):
            seq = list(map(int, input().split()))
            t_seq += seq
            for index in range(0, len(seq), 2):
                current_seq = []
                last_index = mul + index + 1
                list(map(lambda x: heapq.heappush(current_seq, x), t_seq[:last_index]))

                for _ in range(len(current_seq) // 2):
                    heapq.heappop(current_seq)
                m_seq.append(heapq.heappop(current_seq))

        print(len(m_seq))
        while len(m_seq):
            print(" ".join(map(str, m_seq[:10])))
            m_seq = m_seq[10:]


t = int(input().strip())
solution2(t)
