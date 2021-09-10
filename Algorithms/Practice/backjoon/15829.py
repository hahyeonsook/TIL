R, M = 31, 1234567891
ALPHA = {}
for index, alpha in enumerate("abcdefghijklmnopqrstuvwxyz"):
    ALPHA[alpha] = index + 1
N = int(input())
S = input()

hash = []
for i, s in enumerate(S):
    hash.append(ALPHA[s] * R ** i)

print(sum(hash) % M)
