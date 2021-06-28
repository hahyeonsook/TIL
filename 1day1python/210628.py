# REF https://www.30secondsofcode.org/python/s/find-key
# 주어진 dict에서 주어진 값을 가진 키 중에서 첫 번째 키를 반환
def find_key(dict, val):
    # next(iterator, [default]) : 주어진 iterator의 __next__() 함수로 다음 item을 반환.
    # default가 주어지면, iterator의 next 값이 없을 경우 default를 반환하고 StopIteration Exception을 발생시키지 않음.
    return next(key for key, value in dict.items() if value == val)


ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
}

print(find_key(ages, 11))  # 'Isabel'

# REF https://www.30secondsofcode.org/python/s/fibonacci
# n 번째까지의 피보나치 수열을 포함한 list를 생성
def fibonacci(n):
    if n <= 0:
        return [0]
    sequence = [0, 1]
    while len(sequence) <= n:
        next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(next_value)
    return sequence


print(fibonacci(7))  # [0, 1, 1, 2, 3, 5, 8, 13]

# REF https://www.30secondsofcode.org/python/s/delay
# ms 밀리 초 후에 주어진 함수를 호출
from time import sleep


def delay(fn, ms, *args):
    # sleep(n) : n초간 중지함.
    # milliseconds는 1초의 1/1,000 이므로 sleep에 n / 1000로 넣어줌.
    sleep(ms / 1000)
    return fn(*args)


delay(lambda x: print(x), 1000, "later")  # prints 'later' after one second

# REF https://www.30secondsofcode.org/python/s/days-from-now
# 오늘로부터 n 일이 지났을 때의 날짜를 계산
from datetime import timedelta, date


def days_from_now(n):
    return date.today() + timedelta(n)


print(days_from_now(5))  # 2021-07-03
