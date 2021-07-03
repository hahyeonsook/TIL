# 스파이들은 매일 다른 옷을 조합하여 입음.
# 서로 다른 옷의 조합의 수를 return

# clothes의 각 행은 [의상의 이름, 의상의 종류]
# 1 <= clothes <= 30
# 같은 이름을 가진 의상은 없음
# clothes는 문자열
# 1 <= len(문자열) <= 20
# 스파이는 하루에 최소 한 개의 의상을 입음

import collections


def solutuion(clothes):
    answer = 1
    clothes_hash = collections.Counter(list(zip(*clothes))[1])
    for key in clothes_hash:
        answer *= clothes_hash[key] + 1
    return answer - 1


clothes1 = [
    ["yellowhat", "headgear"],
    ["bluesunglasses", "eyewear"],
    ["green_turban", "headgear"],
]
clothes2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

print(solutuion(clothes1))
print(solutuion(clothes2))

# 정확성: 100.0

import collections
from functools import reduce


def solution(clothes):
    return (
        reduce(
            lambda x, y: x * (y + 1),
            collections.Counter(list(zip(*clothes))[1]).values(),
            1,
        )
        - 1
    )


print(solutuion(clothes1))
print(solutuion(clothes2))
