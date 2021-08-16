# REF https://www.30secondsofcode.org/python/s/rgb-to-hex
# RGB 구성요소의 값을 16진수 색상 코드로 변환하라.

# https://brunch.co.kr/@yoojinleem/8
# https://cyber0946.tistory.com/76


def rgb_to_hex(r, g, b):
    # ':' 뒤에 정수를 전달하면 해당 필드의 최소 문자 폭이 된다. 열을 줄 맞춤할 때 편리하다.
    # #4286f4 -> # 42(R) 86(G) f4(B)
    #            # 4(Major Color)2(Minor Color)
    # 각 색깔 코드의 앞과 뒤는 Major Color, Minor Color라고 한다.
    # 02(최소 2자리 숫자를 사용하고 0을 사용하여 길이를 채움)ㅌ(소문자 16진수를 의미)
    # #을 붙이면 0x/0X 접두사를 붙임
    return ("{:02x}" * 3).format(r, g, b)


print(rgb_to_hex(255, 165, 1))  # 'FFA501'

# REF https://www.30secondsofcode.org/python/s/pluck
# dict의 list에서 주어진 key에 해당하는 값을 list로 반환


def pluck(lst, key):
    return [x.get(key) for x in lst]


simpsons = [
    {"name": "lisa", "age": 8},
    {"name": "homer", "age": 36},
    {"name": "marge", "age": 34},
    {"name": "bart", "age": 10},
]
print(pluck(simpsons, "age"))  # [8, 36, 34, 10]


# https://www.30secondsofcode.org/python/s/find-parity-outliers
# https://takeuu.tistory.com/176
# 주어진 리스트에서 이상 패리티 값을 찾아 반환하라.

from collections import Counter


def find_parity_outliers(nums):
    return [
        x
        for x in nums
        # %2해서 가장 많이 나온 값이 x%2와 같지 않으면 x를 list에 포함함.
        #           n%2는 0 또는 1이 나옴. o 또는 1 이 나온 값의 갯수를 튜플의 리스트 형태로 반환함
        if x % 2 != Counter([n % 2 for n in nums]).most_common()[0][0]
    ]


print(find_parity_outliers([1, 2, 3, 4, 6]))  # [1, 3]
