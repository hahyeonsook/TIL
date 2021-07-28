# REF https://www.30secondsofcode.org/python/s/max-element-index
# 리스트에서 가장 큰 값의 인덱스를 반환
def max_element_index(arr):
    # max는 가장 큰 값을 반환
    # index 의 TC는 O(N)
    # max 의 TC는 O(N)
    return arr.index(max(arr))


print(max_element_index([5, 8, 9, 7, 10, 3, 0]))  # 4

# REF https://www.30secondsofcode.org/python/s/max-n
# 리스트에서 큰 순서대로 n개의 값을 반환
def max_n(lst, n=1):
    # sorted는 새로운 list를 반환, list.sort()는 해당 리스트의 값을 바꾸고 None 반환
    # list.sort()는 sorted보다 빠르다.
    # lst.sort(reverse=True)[:n]을 할 경우, 슬라이싱을 None에 한 것이 되므로 오류가 일어난다.
    # TypeError: 'NoneType' object is not subscriptable
    return sorted(lst, reverse=True)[:n]


print(max_n([1, 2, 3]))  # [3]
print(max_n([1, 2, 3], 2))  # [3, 2]

# REF https://www.30secondsofcode.org/python/s/median
# 숫자로 구성된 리스트 값에서 중앙 값을 반환
def median(lst):
    lst.sort()
    lst_length = len(lst)
    # int()는 숫자의 내림 값을 반환한다.
    # 리스트의 길이가 짝수이면 리스트의 값에는 중앙 값이 없을 것이므로 구해준다.
    if lst_length % 2 == 0:
        return (lst[int(lst_length / 2) - 1] + lst[int(lst_length / 2) + 1]) / 2
    # 리스트의 길이가 홀수이면 리스트 가운데 있는 값이 중앙 값이므로 반환한다.
    else:
        return lst[int(lst_length / 2)]


print(median([1, 2, 3]))  # 2
print(median([1, 2, 3, 4]))  # 2.5

# REF
# 주어진 함수를 리스트의 각 값에 적용한 후 그 중 최소 값을 반환
def min_by(lst, fn):
    return min(map(fn, lst))


print(min_by([{"n": 4}, {"n": 2}, {"n": 8}, {"n": 6}], lambda v: v["n"]))  # 2
