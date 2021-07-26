# REF https://www.30secondsofcode.org/python/s/index-of-all
# 리스트 안에서 요소가 발생하는 모든 경우의 인덱스를 리스트로 반환하라.
def index_of_all(lst, value):
    return [i for i, x in enumerate(lst) if x == value]


# REF https://www.30secondsofcode.org/python/s/dict-to-list
# dictionary를 tuple의 list로 변환하라.
def dict_to_list(d):
    return list(d.items())


d = {"one": 1, "three": 3, "five": 5, "two": 2, "four": 4}
print(dict_to_list(d))
# [('one', 1), ('three', 3), ('five', 5), ('two', 2), ('four', 4)]
