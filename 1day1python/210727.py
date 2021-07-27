# REF https://www.30secondsofcode.org/python/s/to-dictionary
# 두 개의 리스트를 딕셔너리로 결합하라. 첫 번째 리스트는 key, 두 번째 리스트는 values이다.


def to_dictionary(keys, values):
    return dict(zip(keys, values))


print(to_dictionary(["a", "b"], [1, 2]))  # { a: 1, b: 2 }


# REF https://www.30secondsofcode.org/python/s/spread
# 주어진 요소들을 새로운 리스트로 펼쳐 flatten 하라.


def spread(arg):
    ret = []
    for i in arg:
        #                isinstance(i, 자료형), i가 자료형인지 결과를 반환
        ret.extend(i) if isinstance(i, list) else ret.append(i)
    return ret


print(spread([1, 2, 3, [4, 5, 6], [7], 8, 9]))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
