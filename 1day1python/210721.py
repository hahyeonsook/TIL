# REF https://www.30secondsofcode.org/python/s/deep-flatten
# list를 깊이 flatten 하라.
from collections.abc import Iterable


def deep_flatten(lst):
    """
    restuls = []

    if isinstance(lst, Iterable):
        for i in lst:
            for a in deep_flatten(i):
                restuls.append(a)
    else:
        return [lst]
    """
    return (
        [a for i in lst for a in deep_flatten(i)]
        if isinstance(lst, Iterable)
        else [lst]
    )


print(deep_flatten([1, [2], [[3], 4], 5]))  # [1, 2, 3, 4, 5]


# REF https://www.30secondsofcode.org/python/s/weighted-average
# 두 개 이상의 가중 평균을 반환하라.
def weighted_average(nums, weights):
    return sum(x * y for x, y in zip(nums, weights)) // sum(weights)


print(weighted_average([1, 2, 3], [0.6, 0.2, 0.3]))  # 1.72727

# REF https://www.30secondsofcode.org/python/s/slugify
# 문자열을 URL 친화적인 슬러그로 변환하라.
import re


def slugify(s):
    s = s.lower().strip()
    #             ^\w: _를 포함한 영숫자 제외
    #                \s: 공백 문자
    s = re.sub(r"[^\w\s-]", "", s)
    #                  +: 1번 이상의 발생
    s = re.sub(r"[\s_-]+", "-", s)
    s = re.sub(r"^-+|-+$", "", s)
    return s
