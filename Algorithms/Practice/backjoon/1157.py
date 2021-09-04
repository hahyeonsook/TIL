import sys, collections

input = sys.stdin.readline

S = input().strip()
S = collections.Counter(S.upper())
rank = S.most_common()
if len(rank) > 1 and rank[0][1] == rank[1][1]:
    print("?")
else:
    print(rank[0][0])
