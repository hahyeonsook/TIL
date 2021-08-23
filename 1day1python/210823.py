# REF https://www.30secondsofcode.org/python/s/merge-dictionaries
# 두 개 이상의 dictionary들을 머지하라.


def merge_dictionaries(*dicts):
    res = dict()

    for d in dicts:
        # REF https://hashcode.co.kr/questions/1009/dictionary%EB%A5%BC-extend%ED%95%98%EB%A0%A4%EB%A9%B4-%EC%96%B4%EB%96%BB%EA%B2%8C-%ED%95%B4%EC%95%BC%EB%90%A0%EA%B9%8C%EC%9A%94
        # dict.update([other])는 other에 key-value로부터 기존의 dict를 업데이트함.
        # other에 기존 키와 중복되는 키가 있으면 그 key에 해당하는 value를 바꾸고,
        # other에 기존 키에 없는 키가 있으면 key-value를 더해줌.
        res.update(d)
    return res


ages_one = {
    "Peter": 10,
    "Isabel": 11,
}
ages_two = {"Anna": 9}
print(merge_dictionaries(ages_one, ages_two))
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }


# REF https://www.30secondsofcode.org/python/s/invert-dictionary
# 유일한 해쉬 값을 사용하여 dict를 인버트하라.


def invert_dictionary(obj):
    return {value: key for key, value in obj.items()}


ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
}
print(invert_dictionary(ages))  # { 10: 'Peter', 11: 'Isabel', 9: 'Anna' }


# REF https://www.30secondsofcode.org/python/s/bifurcate
# 주어진 filter 리스트의 결과를 기반으로 값들을 두 그룹으로 나눠라.


def bifurcate(lst, filter):
    return [
        [x for x, flag in zip(lst, filter) if flag],
        [x for x, flag in zip(lst, filter) if not flag],
    ]


print(bifurcate(["beep", "boop", "foo", "bar"], [True, True, False, True]))
# # [ ['beep', 'boop', 'bar'], ['foo'] ]
