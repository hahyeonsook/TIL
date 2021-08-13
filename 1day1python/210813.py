# REF https://www.30secondsofcode.org/python/s/to-roman-numeral
# 정수를 로마 숫자 표현 방식으로 변환하라.


def to_roman_numeral(num):
    lookup = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    res = ""
    for (n, roman) in lookup:
        # divmod(num, n) == (num//n, num%n)
        (d, num) = divmod(num, n)
        res += roman * d
    return res


print(to_roman_numeral(3))  # 'III'
print(to_roman_numeral(11))  # 'XI'
print(to_roman_numeral(1998))  # 'MCMXCVIII'


# REF https://www.30secondsofcode.org/python/s/sum-of-powers
# start~end 까지 모든 숫자의 거듭제곱의 합을 반환하라.


def sum_of_powers(end, power=2, start=1):
    return sum([(i) ** power for i in range(start, end + 1)])


print(sum_of_powers(10))  # 385
print(sum_of_powers(10, 3))  # 3025
print(sum_of_powers(10, 3, 5))  # 2925


# REF https://www.30secondsofcode.org/python/s/sort-dict-by-key
# 주어진 dict를 key 값으로 정렬하라.


def sort_dict_by_key(d, reverse=False):
    # dict.items()는 튜플의 리스트 값으로 반환된다.
    # 이때, 튜플의 짝이 (키, 값)으로 되어있으므로, 이 튜플의 리스트를 정렬하면 key 값으로 정렬된다.
    return dict(sorted(d.items(), reverse=reverse))


d = {"one": 1, "three": 3, "five": 5, "two": 2, "four": 4}
print(sort_dict_by_key(d))  # {'five': 5, 'four': 4, 'one': 1, 'three': 3, 'two': 2}
print(sort_dict_by_key(d, True))
# {'two': 2, 'three': 3, 'one': 1, 'four': 4, 'five': 5}
