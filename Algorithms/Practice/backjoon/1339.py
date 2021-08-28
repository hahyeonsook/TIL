import sys, collections

input = sys.stdin.readline


def solution(N):
    words = []
    alpha_cnt = collections.defaultdict(int)
    for _ in range(N):
        words.append(input().strip())
        for index, char in enumerate(words[-1]):
            n = len(words[-1]) - index - 1
            alpha_cnt[char] += 10 ** n
    ans = 0
    num = 9
    for char, cnt in sorted(alpha_cnt.items(), key=lambda x: -x[1]):
        ans += num * cnt
        num -= 1

    return ans


print(solution(int(input().strip())))
