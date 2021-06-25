# REF https://www.30secondsofcode.org/python/s/cast-list
# 주어진 값이 리스트가 아닐 경우 리스트로 캐스트
def cast_list(val):
    # isinstance() : 두 번째 인자로 주어진 값이 첫 번째 인자의 클래스 이름인지 True/False
    return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]


print(cast_list("foo"))  # ['foo']
print(cast_list([1]))  # [1]
print(cast_list(("foo", "bar")))

# REF https://www.30secondsofcode.org/python/s/pad
# 주어진 길이보다 문자열의 길이가 짧을 경우, 주어진 문자를 사용하여 길이만큼 패딩
from math import floor


def pad(s, length, char="@"):
    # rjust(width, [fillchar]) : 문자열의 길이가 width이 안될 경우 width가 될만큼 오른쪽에 fillchar로 채움
    # ljust(width, [fillchar]) : 왼쪽에 fillchar로 채움

    # 우선 문자열을 반으로 나눠서 생각함.
    # foo | bar, 그리고 앞의 반에서 우선 채우고 남은 뒤의 값을 채움.
    return s.rjust(floor((len(s) + length) / 2), char).ljust(length, char)


print(pad("cat", 8))  # '  cat   '
print(pad("42", 6, "0"))  # '004200'
print(pad("foobar", 3))  # 'foobar'

# REF https://www.30secondsofcode.org/python/s/key-of-min
# 딕셔너리에서 최소 값을 가진 키를 반환
def key_of_min(d):
    # dict.get은 키를 통해 값을 반환하는 함수
    return min(d, key=d.get)


print(key_of_min({"a": 4, "b": 0, "c": 13}))  # b

# REF https://www.30secondsofcode.org/python/s/key-of-max
# 딕셔너리에서 최대 값을 가진 키를 반환
def key_of_max(d):
    return max(d, key=d.get)


print(key_of_max({"a": 4, "b": 0, "c": 13}))  # c
