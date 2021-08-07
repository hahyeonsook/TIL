# REF https://www.30secondsofcode.org/python/s/every
# 주어진 list의 값들로 주어진 함수를 실행한 값이 모두 True인지 확인하라.


def every(lst, fn=lambda x: x):
    return all(map(fn, lst))


print(every([4, 2, 3], lambda x: x > 1))  # True
print(every([1, 2, 3]))  # True

# REF https://www.30secondsofcode.org/python/s/symmetric-difference
# 두 iterable들의 중복없는 대칭차집합을 반환하라.


def symmetric_difference(a, b):
    (_a, _b) = set(a), set(b)
    return [item for item in a if item not in _b] + [
        item for item in _b if item not in _a
    ]


print(symmetric_difference([1, 2, 3], [1, 2, 4]))  # [3, 4]


# REF https://www.30secondsofcode.org/python/s/map-values
# 주어진 dict의 키와 값으로 제공된 함수를 실행하고 반환된 값으로 새로운 dict를 만들어 반환하라.


def map_values(obj, fn):
    return dict((k, fn(v)) for k, v in obj.items())


users = {"fred": {"user": "fred", "age": 40}, "pebbles": {"user": "pebbles", "age": 1}}
print(map_values(users, lambda u: u["age"]))  # {'fred': 40, 'pebbles': 1}
