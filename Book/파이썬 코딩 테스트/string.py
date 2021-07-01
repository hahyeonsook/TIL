import sys

input = sys.stdin.readline


def isPalindrome(s: str) -> bool:
    strs = []

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


print(isPalindrome("A man, a plan, a canal: Panama"))


from collections import deque


def isPalindrome(s: str) -> bool:

    strs = deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))

import re


def isPalindrome(s: str) -> bool:

    s = s.lower()
    # 정규식 표현으로 문자열을 찾은 후 바꿈
    s = re.sub("[^a-z0-9]", "", s)

    return s == s[::-1]


# 문자열 슬라이싱은 매우 바르다.
print(isPalindrome("A man, a plan, a canal: Panama"))


def reverseString(s: list[str]) -> None:
    s.reverse()


# 요구 조건을 얼마나 깔끔하게 처리할 수 있는지
def reorderLogFiles(logs: list[str]) -> list[str]:
    letters, digits = [], []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append()
        else:
            letters.append()

    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분하지 않으며, 구두점 또한 무시한다.
from collections import defaultdict, Counter

paragraph = "bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    words = [
        word
        for word in re.sub("[^\w]", " ", paragraph).lower().split()
        if word not in banned
    ]

    counts = Counter(words)
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    return counts.most_common(1)[0][0]


print(mostCommonWord(paragraph, banned))


def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    words = [
        word
        for word in re.sub("[^\w]", " ", paragraph).lower().split()
        if word not in banned
    ]

    counts = defaultdict(int)
    for word in words:
        counts[word] += 1

    return max(counts, key=counts.get)


print(mostCommonWord(paragraph, banned))

# 애너그램
# 일종의 언어유희로 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것
from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    # 애너그램 관계인 단어들을 정렬하면 서로 같은 값을 갖게 됨.
    for word in strs:
        # join은 list의 각 값들을 합쳐서 출력하는 함수
        anagrams["".join(sorted(word))].append(word)
    print(anagrams)
    return list(anagrams.values())


print(groupAnagrams(strs))

# sort() : 제자리 정렬(in-place sort)
#          입력을 출력으로 덮어 쓰기 때문에 별도의 추가 공간이 필요하지 않으며 리턴 값이 없음.

# sorted()
# Timsort를 사용함.
# 실제 데이터는 대부분 이미 정렬되어 있을 것이다라고 가정하고 실제 데이터에서 고성능을 낼 수 있도록 설계한 알고리즘.
# 삽입 정렬과 병합 정렬을 휴리스틱하게 적절히 조합해 사용하는 정렬 알고리즘.
# 자바, 스위프드 등의 개발 언어와 안드로이드, 크롬 등의 플랫폼에까지 다양하게 영향을 미쳤다.

# 가장 긴 팰린드롬 부분 문자열을 출력

# 중앙을 중심으로 확장하는 풀이
def longestPalindrome(s: str) -> str:
    # 팰린드롬 판별 및 투 포인터 확장
    # 중앙을 중심으로 확장한다는 게 right 인덱스 값을 기준으로 확장한다는 거임.
    # s[left] == s[right] 이면 left는 0으로 right는 len(s)로 가까워지면서 값을 검사함.
    def expand(left: int, right: int) -> str:
        # left는 최소값이 -1임. 하지만 return 할 때, s[left+1] 하므로 0부터 값이 감.
        # right는 값을 비교할 인덱스
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ""
    # 슬라이싱 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result


print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
