# REF
# 리스트에서 작은 순서대로 N개의 값을 반환 (오름차순으로 정렬)
# N이 리스트의 길이보다 크거나 같으면 원래 리스트를 반환
def min_n(lst, n=1):
    # sorted에서 reverse 의 default는 False이다.
    # 슬라이싱에서 [n:m] 은 n 이상 m 미만이다.
    # 하지만 배열의 인덱스는 0 부터 (m-1) 까지 이므로 m 미만이더라도 모든 값을 포함한다.
    return sorted(lst)[:n]


print(min_n([1, 2, 3]))  # [1]
print(min_n([1, 2, 3], 2))  # [1, 2]
print(min_n([1, 2, 3], 3))  # [1, 2, 3]


# REF
# 리스트에서 개수가 가장 많은 값을 반환
def most_frequent(lst):
    # Callable object란 함수처럼 호출될 수 있는 객체를 말한다.
    # key는 func, literalb한 값을 받아서
    return max(set(lst), key=lst.count)


print(most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]))

# REF https://www.30secondsofcode.org/python/s/n-times-string
# 주어진 횟수만큼 동일한 문자열을 출력
def n_times_string(s, n):
    # 문자에 * 연산을 사용하면 반복할 수 있음.
    return s * n


print(n_times_string("py", 4))  # 'pypypypy'


# REF https://www.30secondsofcode.org/python/s/offset
# 주어진 요소의 개수만큼을 리스트의 끝으로 이동
def offset(lst, offset):
    #         offset=2
    # [   1,    2,    3,    4,    5   ]
    #                     offset=-2
    return lst[offset:] + lst[:offset]


print(offset([1, 2, 3, 4, 5], 2))  # [3, 4, 5, 1, 2]
print(offset([1, 2, 3, 4, 5], -2))  # [4, 5, 1, 2, 3]


# REF
# radian에서 degree로 변환
from math import pi


def rads_to_degrees(rad):
    return (rad * 180.0) / pi


print(rads_to_degrees(pi / 2))  # 90.0

# REF
# 문자열을 거꾸로 뒤집어라
def reverse_string(s):
    return s[::-1]


print(reverse_string("snippet"))  # "teppins"
