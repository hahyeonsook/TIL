import sys

input = sys.stdin.readline

cities = list(map(int, input().split()))
distances = [[0 for _ in range(5)] for _ in range(5)]

for r in range(5):
    for c in range(5):
        if r == c:
            continue
        if r < c:
            distances[r][c] = sum(cities[r:c])
        else:
            distances[r][c] = sum(cities[c:r])
    print(*distances[r])
