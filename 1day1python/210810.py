# REF https://www.30secondsofcode.org/python/s/find-last
# 함수와 리스트가 주어질 때, 함수를 만족하는 리스트의 마지막 값을 찾아 반환하라.


def find_last(lst, fn):
    # (리스트 컴프리헨션): 제너레이터, 연속된 값을 차례로 생성해서 돌려줌(yield)
    # print(리스트 컴프리헨션) -> generator object로 나옴
    # 여기서는 next 안에 generator object를 넣은 것임
    # 그래서 next는 해당 generator에 해당하는 가장 처음 값을 돌려주는 것
    return next(x for x in lst[::-1] if fn(x))


print(find_last([1, 2, 3, 4], lambda n: n % 2 == 1))  # 3

# REF https://www.30secondsofcode.org/python/s/find
# 함수와 리스트가 주어질 때, 함수를 만족하는 리스트의 첫번째 값을 찾아 반환하라.


def find(lst, fn):
    return next(x for x in lst if fn(x))


print(find([1, 2, 3, 4], lambda n: n % 2 == 1))  # 1


# REF https://www.30secondsofcode.org/python/s/average-by
# 주어진 함수에 리스트의 각 요소를 매핑한 후, 값의 평균을 구하라.
def average_by(lst, fn=lambda x: x):
    return sum(map(fn, lst), 0.0) / len(lst)


print(average_by([{"n": 4}, {"n": 2}, {"n": 8}, {"n": 6}], lambda x: x["n"]))  # 5.0
