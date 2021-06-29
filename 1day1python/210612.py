# REF https://www.30secondsofcode.org/python/s/sample
# 리스트에서 랜덤하게 값을 반환
from random import randint


def sample(lst):
    return lst[randint(0, len(lst) - 1)]


print(sample([3, 7, 9, 11]))


# REF
# 두 리스트에 모두 있는 값들을 반환
def similarity(a, b):
    # return list(set(a) & set(b))
    return [item for item in a if item in b]


print(similarity([1, 2, 3], [1, 2, 4]))  # [1, 2]

# REF
# 여러 줄로 되어 있는 문자열을 리스트로 분할
def split_lines(s):
    return s.split("\n")


# \n이 구분자라서 뒤에 ''까지 나온 모양
print(
    split_lines("This\nis a\nmultiline\nstring.\n")
)  # ['This', 'is a', 'multiline', 'string.', '']
print(
    split_lines("This\nis a\nmultiline\nstring.")
)  # ['This', 'is a', 'multiline', 'string.']


# REF
# 주어진 함수를 리스트의 각 값에 적용한 뒤, 합계를 반환
def sum_by(lst, fn):
    return sum(map(fn, lst))


print(sum_by([{"n": 4}, {"n": 2}, {"n": 8}, {"n": 6}], lambda v: v["n"]))  # 20
