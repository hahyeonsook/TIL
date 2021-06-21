# REF https://www.30secondsofcode.org/python/s/key-in-dict
# 주어진 key 가 dict에 있는지 반환


def key_in_dict(d, key):
    return key in d


d = {"one": 1, "three": 3, "five": 5, "two": 2, "four": 4}
print(key_in_dict(d, "three"))  # True


# REF https://www.30secondsofcode.org/python/s/is-weekend
# 주어진 날짜가 주말인지 반환
from datetime import datetime


def is_weekend(d=datetime.today()):
    # 월요일 1, 화요일 2, 수요일 3, 목요일 4, 금요일 5, 토요일 6, 일요일 7
    # return d.isoweekday()
    # 정수로 요일을 반환
    # 월요일 0, 화요일 1, 수요일 2, 목요일 3, 금요일 4, 토요일 5, 일요일 6
    return d.weekday() > 4


from datetime import date

print(is_weekend(date(2020, 10, 25)))  # True
print(is_weekend(date(2020, 10, 28)))  # False

# REF https://www.30secondsofcode.org/python/s/is-prime
# 제공된 integer가 소수인지 반환
# 숫자가 0 or 1 or 음수 or 2의 배수이면 False
from math import sqrt


def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False

    # 3부터 n의 제곱근까지 모든 수로 나누어 본다.
    # 나누어 떨어지지 않으면, 소수이다. -> n%i != 0 이면 소수
    # 짝수는 소수가 아니므로 위의 if 절에서 걸러지고,
    #                                                      짝수로 나뉘어질 경우, 짝수이므로 위에서 걸러지기 때문에 계산하지 않는다.
    #                           3부터 모든 홀수 값으로 나누어 떨어지는지 계산하고, 나머지가 0이 아니면 소수로 판별한다.
    # return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))

    # all(): 인자로 받은 반복 가능한 자료형의 모든 요소가 True이면 True를 반환
    #        iterable한 값이 모두 0 이면 False를 반환
    # range(시작숫자, 종료숫자, step)
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))


# 에라토스테네스의 체
# 소수란, 2보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수
# 2부터 n-1까지 돌려보면 된다 -> O(n)
# 에라토스테네스의 체 -> O(nloglogn)
# 범위에 대한 소수 판별에 유리.
# 1. 2부터 n까지의 모든 자연수를 나열한다.
# 2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
# 3. 남은 수 중에서 i의 배수를 모두 제거한다.(i는 제거하지 않는다.)
# 4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.
def is_prime_number(n):
    array = [True for i in range(n + 1)]  # 모든 수가 소수(True) 인 것으로 초기화

    # 에라토스테네스의 체
    for i in range(2, int(sqrt(n)) + 1):  # 2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True:  # i가 소수인 경우
            # i를 제외한 i의 모든 배수 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
        return [i for i in range(2, n + 1) if array[i]]


print(is_prime_number(26))
