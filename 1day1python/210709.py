# REF https://www.30secondsofcode.org/python/s/have-same-contents
# 순서와 관계 없이 두 리스트에 동일한 요소가 포함되어 있는지 확인하라.
def have_same_contents(a, b):
    # set은 집합으로 원소의 중복을 없앰.
    for v in set(a + b):
        # count() : 찾고자 하는 항목이 리스트에 몇 개 들었는지 확인
        if a.count(v) != b.count(v):
            return False
    return True


print(have_same_contents([1, 2, 4], [2, 4, 1]))  # True
print(have_same_contents([1, 2, 4, 4], [2, 4, 1]))  # False

# REF https://www.30secondsofcode.org/python/s/gcd
# 숫자들의 리스트의 최대공약수를 구하라.
from functools import reduce
from math import gcd as _gcd


def gcd(numbers):
    # reduce() : iterable한 변수를 fn 누적 적용하여 단일 값으로 리턴하는 함수
    # math.gcd() : python 3.5 최대공약수를 구하는 함수
    # recude(_gcd, numbers) = _gcd(_gcd(_gcd(numbers[0]), numbers[1]), numbers[2])
    return reduce(_gcd, numbers)


print(gcd([8, 36, 28]))  # 4

# REF https://www.30secondsofcode.org/python/s/to-iso-date
# ISO-8601 https://ko.wikipedia.org/wiki/ISO_8601
# 날짜를 ISO-8601 표기로 변환하라.
from datetime import datetime


def to_iso_date(d):
    return d.isoformat()


print(to_iso_date(datetime(2021, 7, 9)))  # 2021-07-09T00:00:00
