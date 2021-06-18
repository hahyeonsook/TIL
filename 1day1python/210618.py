# REF
# 주어진 리스트의 고유한 값들을 반환
def unique_elements(lst):
    return list(set(lst))


print(unique_elements([1, 2, 2, 3, 4, 5, 3]))  # [1, 2, 3, 4, 5]


# REF
# 딕셔너리의 모든 값을 리스트로 반환
def values_only(flat_dict):
    # flat_dict.values()
    # dict_values([10, 11, 9])
    # >>> flat_dict.items()
    # dict_items([('Peter', 10), ('Isabel', 11), ('Anna', 9)])
    # >>> flat_dict.keys()
    # dict_keys(['Peter', 'Isabel', 'Anna'])
    return list(flat_dict.values())


ages = {"Peter": 10, "Isabel": 11, "Anna": 9}
print(values_only(ages))  # [10, 11, 9]


# REF https://www.30secondsofcode.org/python/s/to-hex
# 주어진 숫자를 16 진수로 반환
def to_hex(dec):
    # ord(c) 문자의 유니코드를 반환, chr 함수의 반대이다.
    # hex(ord(c)) # string hex로 변환
    return hex(dec)


print(to_hex(41))  # 0x29
print(to_hex(332))  # 0x14c

# REF https://www.30secondsofcode.org/python/s/to-binary
# 주어진 숫자를 2 진수로 반환
def to_binary(dec):
    return bin(dec)


print(to_binary(100))  # 0b1100100
print(100 >> 2)  # 25
print(to_binary(25))  # 0b11001
print(100 << 2)  # 400
print(to_binary(400))  # 0b110010000

# REF https://www.30secondsofcode.org/python/p/1
# 반복이나 순서 없이 n개의 항목에서 k개를 선택하는 방법의 수를 계산
# 반복 가능한 객체에서 중복을 허용하지 않고 뽑는 것은 조합
from math import comb


def binomial_coefficient(n, k):
    return comb(n, k)


print(binomial_coefficient(8, 2))  # 28

# REF https://www.30secondsofcode.org/python/s/factorial
# 주어진 숫자의 팩토리얼을 계산
def factorial(num):
    if not ((num >= 0)) and (num % 1 == 0):
        raise Exception("Number can't be floating point or negative.")
    return 1 if num == 0 else num * factorial(num - 1)


print(factorial(6))  # 720
