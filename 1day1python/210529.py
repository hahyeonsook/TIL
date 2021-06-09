# REF https://www.30secondsofcode.org/python/s/difference
# 두 리스트의 차집합.
def difference(a, b):
    # 집합에는 중복이 없기 때문에 set을 쓴 게 아닐까 싶다.
    # 그럼 출력 값도 set으로 변환해서 return 해야하지 않을까?
    _b = set(b)
    return [item for item in a if item not in b]


print([1, 2, 3], [1, 2, 4])  # [3]

# REF https://www.30secondsofcode.org/python/s/digitize
# 한 숫자를 숫자의 리스트로 변환.
def digitize(n):
    # map(): 리스트 요소를 지정된 함수로 처리 해줌(원본 리스트를 변경하지 않고, 새 리스트를 생성함.).
    # 문자열은 리스트처럼 처리가 되므로, str로 변환한 후 map을 적용시킴.
    return list(map(int, str(n)))


print(digitize(123))  # [1, 2, 3]

# REF https://www.30secondsofcode.org/python/s/drop
# 왼쪽에서부터 n개의 요소가 제거된 리스트를 반환.
def drop(a, n=1):
    # python 슬라이싱, a:b => a이상 b미만
    return a[n:]


drop([1, 2, 3])  # [2, 3]
drop([1, 2, 3], 2)  # [3]
# 에러를 안일으키는 구나.
drop([1, 2, 3], 42)  # []

# REF https://www.30secondsofcode.org/python/s/drop-right
# 오른쪽에서부터 n개의 요소가 제거된 리스트 반환.
def drop_right(a, n=1):
    return a[:-n]


drop_right([1, 2, 3])  # [1, 2]
drop_right([1, 2, 3], 2)  # [1]
# 에러를 안일으키는 구나.
drop_right([1, 2, 3], 42)  # []
