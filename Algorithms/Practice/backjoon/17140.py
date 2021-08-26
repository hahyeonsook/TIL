import sys
from collections import Counter, defaultdict

input = sys.stdin.readline


def solution(R, C, K):
    maps = [[0 for _ in range(101)] for _ in range(101)]
    for r in range(3):
        row = list(map(int, input().split()))
        for c in range(len(row)):
            maps[r][c] = row[c]

    def r_operation(m, n):
        rows = defaultdict(list)
        for r in range(m):
            row = sorted(Counter(maps[r]).items(), key=lambda x: (x[1], x[0]))
            for column in row:
                if column[0] != 0:
                    rows[r].extend(list(column))
            n = max(n, len(rows[r]))

        for r in range(m):
            while len(rows[r]) < n:
                rows[r].append(0)
            for c in range(n):
                maps[r][c] = rows[r][c]
        return m, n

    def c_operation(m, n):
        tmp = list(map(list, zip(*maps)))
        columns = defaultdict(list)
        for c in range(n):
            column = sorted(Counter(tmp[c]).items(), key=lambda x: (x[1], x[0]))
            for row in column:
                if row[0] != 0:
                    columns[c].extend(list(row))
            m = max(m, len(columns[c]))

        for c in range(n):
            while len(columns[c]) < m:
                columns[c].append(0)
            for r in range(m):
                maps[r][c] = columns[c][r]
        return m, n

    time = 0
    m, n = 3, 3
    while maps[R - 1][C - 1] != K:
        if m >= n:
            m, n = r_operation(m, n)
        else:
            m, n = c_operation(m, n)

        time += 1
        if time > 100:
            return -1
    return time


R, C, K = map(int, input().split())
print(solution(R, C, K))
