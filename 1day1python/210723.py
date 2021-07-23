# REF https://www.30secondsofcode.org/python/s/lcm
# 숫자의 최소 공배수를 반환하라.
from functools import reduce
from math import gcd


def lcm(numbers):
    return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)


print(lcm([12, 7]))  # 84
print(lcm([1, 3, 4, 5]))  # 60

# REF https://www.30secondsofcode.org/python/s/is-anagram
# 한 문자열이 다른 문자열의 애너그램인지 확인하라.
from collections import Counter


def is_anagram(s1, s2):
    return Counter(c.lower() for c in s1 if c.isalnum()) == Counter(
        c.lower() for c in s2 if c.isalnum()
    )


print(is_anagram("#anagram", "Nag a ram!"))  # True
