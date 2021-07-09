# REF https://www.acmicpc.net/problem/1213
# 2초, 40,000,000
# 실버 4

# 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들어라.

# 영어 이름이 여러개일 경우, 사전순으로 앞서는 것을 출력하라.

import collections


def solution(name):
    odd_alpha = None
    palindrome = []
    alphas = collections.Counter(sorted(name))

    for alpha in alphas:
        if alphas[alpha] % 2 != 0:
            if odd_alpha:
                return "I'm Sorry Hansoo"
            odd_alpha = alpha
        palindrome += [alpha] * (alphas[alpha] // 2)
    if odd_alpha:
        palindrome = palindrome + [odd_alpha] + palindrome[::-1]
    else:
        palindrome = palindrome + palindrome[::-1]
    return "".join(palindrome)


print(solution("aaabb"))
print(solution("AABBCCCDD") == "ABCDCDCBA")
print(solution("AAABB") == "ABABA")
