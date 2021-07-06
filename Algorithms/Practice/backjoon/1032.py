import sys

input = sys.stdin.readline
n = int(input().strip())
cmd = input().strip()
common_word = cmd[:]
for _ in range(n - 1):
    cmd = input().strip()

    for i in range(len(common_word)):
        if common_word[i] != "?" and common_word[i] != cmd[i]:
            common_word = common_word[:i] + "?" + common_word[i + 1 :]

print(common_word)

# 반례
# 입력
# 3
# a
# b
# b
# ?가 나와야하는데 b가 나옴.

# 반례
# 입력
# 3
# abc
# bbc
# aba
# 출력
# ???
# 정답 : ?b?
