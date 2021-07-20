# REF https://www.30secondsofcode.org/python/s/powerset
# 주어진 iterable의 멱집합을 반환하라.
# 멱집합: 주어진 집합의 모든 부분 집합들로 구성된 집합.
from itertools import chain, combinations


def powerset(iterable):
    s = list(iterable)
    #       combinations(list, number): number의 엘리먼트를 가진 집합을 반환.
    #           chain(): iterables로 연결함.
    #           chain.from_iterables(): 2차원 리스트를 1차원 리스트로 연결함.
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))


print(powerset([1, 2]))  # [(), (1,), (2,), (1, 2)]

# REF https://www.30secondsofcode.org/python/s/hamming-distance
# 두 변수의 해밍 거리를 계산하라.
# 해밍 거리
# 문자열의 경우, 두 문자열의 같은 위치에 있는 두 문자를 비교하여 다른 문자의 수를 세는 것.
# 이진수의 경우 다른 위치의 비트 개수를 세는 것.
def hamming_distance(a, b):
    #           ^ : XOR operator, 피연산자의 값이 같지 않으면 1을 출력.
    #      bin(): 이진수 문자열로 리턴.
    #             파이썬에서는 기본적으로 10진수 형태로 숫자를 표현하기 때문에 다른 진수의 형태로 숫자를 표현하려면 숫자 앞에 접두어를 붙여줘야 함.
    #             2진수: 0b, 8진수: 0o, 16진수: 0x
    return bin(a ^ b).count("1")


print(hamming_distance(2, 3))  # 1

# REF https://www.30secondsofcode.org/python/s/from-iso-date
# ISO-8601 표기인 날짜를 변환하라.

from datetime import datetime


def from_iso_date(d):
    return datetime.fromisoformat(d)


print(from_iso_date("2021-07-20T15:13:46.000000"))  # 2021-07-20 15:13:46

# REF https://www.30secondsofcode.org/python/s/flatten
# list의 list를 flatten 하라.


def flatten(lst):
    # for y in lst:
    #   for x in y:
    #       x
    # 아래의 list 내포 이중 for 문은 위의 이중 for 문과 같다.
    return [x for y in lst for x in y]


print(flatten([[1, 2, 3, 4], [5, 6, 7, 8]]))  # [1, 2, 3, 4, 5, 6, 7, 8]
