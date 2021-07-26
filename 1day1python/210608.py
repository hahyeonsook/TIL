# REF https://www.30secondsofcode.org/python/s/initial
# 마지막 값을 제외한 모든 값을 반환
def initial(lst):
    return lst[:-1]


print(initial([1, 2, 3]))  # [1, 2]

# REF https://www.30secondsofcode.org/python/s/initialize-list-with-range
# 주어진 범위만큼의 리스트, 각 값은 step 만큼 커짐
def initialize_list_with_range(end, start=0, step=1):
    return list(range(start, end + 1, step))


print(initialize_list_with_range(5))  # [0, 1, 2, 3, 4, 5]
print(initialize_list_with_range(7, 3))  # [3, 4, 5, 6, 7]
print(initialize_list_with_range(9, 0, 2))  # [0, 2, 4, 6, 8]

# REF https://www.30secondsofcode.org/python/s/initialize-list-with-values
# 주어진 값으로 채운 리스트
def initialize_list_with_values(n, val=0):
    return [val for x in range(n)]


print(initialize_list_with_values(5, 2))  # [2, 2, 2, 2, 2]

# REF https://www.30secondsofcode.org/python/s/intersection
# 두 리스트에 존재하는 값으로 리스트를 만듦
def intersection(a, b):
    _a, _b = set(a), set(b)
    # & 연산자는 set의 교집합 연산
    # 합집합 연산: |
    # 차집합 연산: -
    # 대칭차집합(XOR): ^ 겹치지 않는 요소
    # list & list -> TypeError: unsupported operand type(s) for &: 'list' and 'list'
    # 논리연산자라면? 이것들은 우선순위에 따라 오름차순으로 정렬된 논리 연산들입니다:
    # x or y => x가 거짓이면 y를 출력, 참이면 x를 출력.
    # x and y => x가 참이면 y를 출력, 거짓이면 x를 출력.
    return list(_a & _b)


print(intersection([1, 2, 3], [4, 3, 2]))  # [2, 3]
