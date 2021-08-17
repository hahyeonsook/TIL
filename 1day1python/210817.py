# https://www.30secondsofcode.org/python/s/find-last-index
# 주어진 리스트에서 주어진 테스트 함수를 만족하는 요소의 인덱스를 찾아라.


def find_last_index(lst, fn):
    # len(lst)-1에서 값을 빼는 이유는, lst를 역전환해서 돌렷기 때문이다.
    return len(lst) - 1 - next(i for i, x in enumerate(lst[::-1]) if fn(x))


print(find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1))  # 2


# https://www.30secondsofcode.org/python/s/chunk-into-n
# 주어진 리스트를 n개의 더 작은 리스트들로 반환하라.

from math import ceil


def chunk_into_n(lst, n):
    size = ceil(len(lst) / n)
    return list(map(lambda x: lst[x * size : x * size + size], list(range(n))))


print(chunk_into_n([1, 2, 3, 4, 5, 6, 7], 4))  # [[1, 2], [3, 4], [5, 6], [7]]

# REF https://www.30secondsofcode.org/python/s/chunk
# 주어진 리스트를 지정된 크기의 작은 목록들로 반환하라.
from math import ceil


def chunk(lst, size):
    return list(
        map(
            lambda x: lst[x * size : x * size + size],
            list(range(ceil(len(lst) / size))),
        )
    )


print(chunk([1, 2, 3, 4, 5], 2))  # [[1, 2], [3, 4], [5]]
