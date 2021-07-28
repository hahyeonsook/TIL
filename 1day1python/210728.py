# REF https://www.30secondsofcode.org/python/s/reverse-number
# 숫자를 reverse 하라.
from math import copysign


def reverse_number(n):
    #      copysign(x, y): x의 크기(절댓값)와 y의 부호를 갖는 float를 반환
    return copysign(float(str(n)[::-1].replace("-", "")), n)


# REF https://www.30secondsofcode.org/python/s/decapitalize
# 문자열의 첫 글자를 바꿔라.


def decapitalize(s, upper_rest=False):
    return "".join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])


print(decapitalize("FooBar"))  # 'fooBar'
print(decapitalize("FooBar", True))  # 'fOOBAR'
