import sys, collections

input = sys.stdin.readline
T = int(input().strip())
for _ in range(T):
    score = input().strip()
    score_cnt = []
    cnt = 0
    for s in score:
        if s == "O":
            cnt += 1
        else:
            cnt = 0
        score_cnt.append(cnt)
    print(sum(score_cnt))
