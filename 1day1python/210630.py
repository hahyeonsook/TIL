# REF https://www.30secondsofcode.org/python/s/days-ago
# 오늘로부터 n 일 후의 날짜를 계산
from datetime import date, timedelta


def days_ago(n):
    return date.today() - timedelta(n)


print(days_ago(5))  # 2021-06-25


# REF https://www.30secondsofcode.org/python/s/arithmetic-progression
# 주어진 양의 정수에서 최대 지정된 제한 값까지 산술 연산에 포함된 숫자의 목록을 생성
def arithmetic_progression(n, lim):
    return list(range(n, lim + 1, n))


print(arithmetic_progression(5, 25))  # [5, 10, 15, 20, 25]

# REF https://www.30secondsofcode.org/python/s/reverse
# 주어진 리스트 또는 문자열을 뒤집어라
def reverse(itr):
    return itr[::-1]


print(reverse([1, 2, 3]))  # [3, 2, 1]
print(reverse("snippet"))  # teppins


# REF https://www.30secondsofcode.org/python/s/includes-any
# 주어진 `values`의 어떤 값이라도`lst` 안에 포함되는지 검사
def includes_any(lst, values):
    for v in values:
        # not in 이 아닌 이유는 any element in values라서
        if v in lst:
            return True
    return False


print(includes_any([1, 2, 3, 4], [2, 9]))  # True
print(includes_any([1, 2, 3, 4], [8, 9]))  # False
