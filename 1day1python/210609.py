# https://www.inflearn.com/course/%EC%99%BC%EC%86%90%EC%BD%94%EB%94%A9-%ED%8C%8C%EC%9D%B4%EC%8D%AC-50%EC%A0%9C/lecture/52717?tab=curriculum
# https://wayhome25.github.io/python/2017/06/14/time-complexity/

# REF
# 첫 번째 숫자가 두 번째 숫자로 나눠 떨어지는지
def is_divisible(dividend, divisor):
    # % 연산자는 나누고 남은 나머지를 반환한다.
    # % 연산자가 비교연산자보다 우선순위가 높으니까 True/False 값이 리턴된다.
    return dividend % divisor == 0


print(is_divisible(6, 2))  # True

# REF
# 주어진 숫자가 짝수인지
def is_even(num):
    return num % 2 == 0


print(is_even(3))  # False

# REF
# 주어진 숫자가 홀수인지
def is_odd(num):
    return num % 2 != 0


print(is_odd(3))  # True

# REF https://www.30secondsofcode.org/python/s/keys-only
# Dictionary의 모든 키를 list로 변환
def keys_only(flat_dict):
    # return [key for key, value in flat_dict.items()]

    # dict.keys()는 <class 'dict_keys'>, list화 하면 ['Peter', 'Isabel', 'Anna']
    # dict.values()는 <class 'dict_values'>, list화 하면 [10, 11, 9]
    # dict.items()는 <class 'dict_items'>, list화 하면 [('Peter', 10), ('Isabel', 11), ('Anna', 9)]
    # O(1)
    return list(flat_dict.keys())


ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
}
print(keys_only(ages))  # ['Peter', 'Isabel', 'Anna']

# REF https://www.30secondsofcode.org/python/s/last
# 리스트의 마지막 값을 반환
def last(lst):
    return lst[-1]


print(last([1, 2, 3]))  # 3

# REF https://www.30secondsofcode.org/python/s/max-by
# 주어진 함수를 리스트의 각 값에 적용한 후 max를 반환
def max_by(lst, fn):
    # O(N) + O(N)
    return max(map(fn, lst))


print(max_by([{"n": 4}, {"n": 2}, {"n": 8}, {"n": 6}], lambda v: v["n"]))  # 8
