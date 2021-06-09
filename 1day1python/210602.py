# REF
# 리스트의 모든 값을 오른쪽에서부터 주어진 함수로 실행
def for_each_right(itr, fn):
    for el in itr[::-1]:
        fn(el)


for_each_right([1, 2, 3], print)  # 3 2 1

# REF
# 리스트에 중복된 값이 있으면 True, 없으면 False
def has_duplicates(lst):
    return len(lst) != len(set(lst))


x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]

print(has_duplicates(x))  # True
print(has_duplicates(y))  # False

# REF
# 리스트에서 첫번째 값을 반환
def head(lst):
    return lst[0]


print(head([1, 2, 3]))  # 1


# REF
# 주어진 숫자가 해당 범위 내에 있는지 확인
def in_range(n, start, end=0):
    # end가 주어지지 않을 경우, end=0 이므로 start보다 end가 작을 경우 end <= n <= start로 계산
    return start <= n <= end if end >= start else end <= n <= start

print(in_range(3, 2, 5)) # True
print(in_range(3, 4)) # True
print(in_range(2, 3, 5)) # False
print(in_range(3, 3)) # False

