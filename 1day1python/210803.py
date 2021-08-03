# REF https://www.30secondsofcode.org/python/s/some
# 주어진 함수에 리스트의 값을 실행시켰을 때, 하나의 값이라도 True를 반환하는지 확인하라.
def some(lst, fn=lambda x: x):
    # any(iterableValue): iterable한 자료형의 element 중 하나라도 True일 경우, True를 반환
    return any(map(fn, lst))


print(some([0, 1, 2, 0], lambda x: x >= 2))  # True
print(some([0, 0, 1, 0]))  # True

# REF https://www.30secondsofcode.org/python/s/longest-item
# 길이를 가진 iterable한 객체 또는 객체들을 사용하여, 가장 긴 하나를 반환하라.

# REF https://brunch.co.kr/@princox/180
# *args: 여러 개의 인자를 튜플 형태로 받기 위한 함수 파라미터
# **kwargs: 여러 개의 인자를 딕셔너리 형태로 받기 위한 함수 파라미터
def longest_item(*args):
    #                key: type func, key를 기준으로 max 값을 찾아서 반환
    return max(args, key=len)


print(longest_item("this", "is", "a", "testcase"))  # 'testcase'
print(longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(longest_item([1, 2, 3], "foobar"))  # 'foobar'

# REF https://www.30secondsofcode.org/python/s/geometric-progression
# start 부터 end 까지의 주어진 범위 내의 숫자를 포함하는 리스트를 반환하라.
# 리스트는 start와 end를 포함하며, 앞 뒤 두 항은 step 비율을 갖는다.
# step이 1로 주어지면, 오류를 반환하라.

# 등비수열
from math import floor, log


def geometric_progression(end, start=1, step=2):
    # 등비수열의 일반항: a * r^(n-1)
    # a = start, r = step, 마지막 항 = end
    # start * step^(n-1) = end
    # step^(n-1) = end/start
    # n-1 = log((end/start), step)
    # n = log((end/start), step) + 1
    # log(): 변수의 자연 로그를 반환
    return [start * step ** i for i in range(floor(log(end / start) / log(step)) + 1)]


print(geometric_progression(256))  # [1, 2, 4, 8, 16, 32, 64, 128, 256]
print(geometric_progression(256, 3))  # [3, 6, 12, 24, 48, 96, 192]
print(geometric_progression(256, 1, 4))  # [1, 4, 16, 64, 256]
