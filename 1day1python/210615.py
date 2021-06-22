# REF https://www.30secondsofcode.org/python/s/tail
# 첫번째 값을 제외한 리스트의 모든 값을 반환
def tail(lst):
    return lst[1:] if len(lst) > 1 else lst


print(tail([1, 2, 3]))  # [2, 3]
print(tail([1]))  # [1]

# REF https://www.30secondsofcode.org/python/s/take
# 앞에서부터 n개의 값을 반환
def take(itr, n=1):
    return itr[:n]


print(take([1, 2, 3], 5))  # [1, 2, 3]
print(take([1, 2, 3], 0))  # []

# REF https://www.30secondsofcode.org/python/s/take-right
# 끝에서부터 n개의 값을 반환
def take_right(itr, n=1):
    # - index는 뒤에서 부터 값에 접근할 때 사용
    return itr[-n:]


print(take_right([1, 2, 3], 2))  # [2, 3]

# REF https://www.30secondsofcode.org/python/s/union
# 두 리스트 중에서 하나의 리스트에라도 존재하는 모든 값을 반환
def union(a, b):
    # 두 리스트를 set으로 만든 후 합집합 연산인 |를 사용한다.
    # return list(set(a) | set(b))
    # 두 리스트를 더한 다음, set 자료형으로 중복을 없애줌.
    return list(set(a + b))


print(union([1, 2, 3], [4, 3, 2]))  # [1, 2, 3, 4]
