# REF https://www.30secondsofcode.org/python/s/months-diff
# 두 날짜 사이의 달 차이를 반환
from math import ceil


def months_diff(start, end):
    # timedelta에는 days, seconds, microseconds 등만 있음.
    # month는 없기 때문에 days로 계산해야 함.
    return ceil((end - start).days / 30)


from datetime import date

print(months_diff(date(2020, 10, 28), date(2020, 11, 25)))  # 1

# REF https://www.30secondsofcode.org/python/s/min-element-index
# 리스트의 값 중 가장 작은 요소의 인덱스를 반환
def min_element_index(lst):
    # list.index는 값의 index를 반환
    return lst.index(min(lst))


print(min_element_index([3, 5, 2, 6, 10, 7, 9]))  # 2

# REF https://www.30secondsofcode.org/python/s/is-contained-in
# 순서에 관계없이 첫 번째 리스트의 값들이 두 번째 리스트에 포함되는지 반환
def is_contained_in(a, b):
    # in은 멤버십 검사 연산.
    # list in list의 경우 list를 하나의 값으로 인식해서 검사한다.
    # list1=[1] in list2=[1, 2, 3] => False
    # list1=[1] in list2=[[1], 1, 2, 3] => True
    # return a in b # False
    """
    for v in set(a):
        # O(2N)
        if a.count(v) > b.count(v):
            return False
    return True
    """
    for v in set(a):
        # O(N)
        if v not in b:
            return False
    return True


print(is_contained_in([1, 4], [2, 4, 1]))  # True
print(is_contained_in([1, 5], [2, 4, 1]))  # False


# REF https://www.30secondsofcode.org/python/s/cumsum
# 부분 합의 리스트를 만들어서 반환
from itertools import accumulate


def cumsum(lst):
    # accumulate(p, [,func]): p0, p0+p1, p0+p1+p2, ...
    return list(accumulate(lst))


print(cumsum(range(0, 15, 3)))  # [0, 3, 9, 18, 30]
