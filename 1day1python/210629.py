# REF https://www.30secondsofcode.org/python/s/when
# testing 함수로 x를 테스트한 후, 값에 따라 함수를 적용
# predicate(x)의 값이 True인지 확인하고 True이면 when_true를 반환하고 그렇지 않으면 x를 반환
def when(predicate, when_true):
    return lambda x: when_true(x) if predicate(x) else x


#                          predicate: x가 짝수인지 검사, when_true: x에 2를 곱함
# predicate와 when_true 함수를 지정한 when을 double_even_numbers에 할당, double_even_numbers는 함수
double_even_numbers = when(lambda x: x % 2 == 0, lambda x: x * 2)
# x 값으로 2를 줌
print(double_even_numbers(2))  # 4
print(double_even_numbers(1))  # 1

# REF https://www.30secondsofcode.org/python/s/transpose
# 2차원 리스트의 행렬을 바꿔라
def transpose(lst):
    # *는 컨테이너 타입의 데이터를 unpacking할 때 사용할 수 있다.
    # list, tuple, dict 형태의 데이터를 unpacking할 수 있다.
    # >>> lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    # >>> print(*lst)
    # [1, 2, 3] [4, 5, 6] [7, 8, 9] [10, 11, 12]
    # >>> headers = {
    # ...   'Accept': 'text/plain',
    # ...   'Content-Length': 348,
    # ...   'Host': 'http://mingrammer.com'
    # ... }
    # >>> print(*headers)
    # Accept Content-Length Host
    return list(zip(*lst))


print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
# [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]


# REF https://www.30secondsofcode.org/python/s/roll
# 지정된 offset 만큼을 리스트의 앞으로 이동
def roll(lst, offset):
    return lst[-offset:] + lst[:-offset]


print(roll([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
print(roll([1, 2, 3, 4, 5], -2))  # [3, 4, 5, 1, 2]

# REF https://www.30secondsofcode.org/python/s/num-to-range
# 한 범위 안의 숫자를 다른 범위의 수로 매핑
def num_to_range(num, inMin, inMax, outMin, outMax):
    # 선형 변환
    # http://daplus.net/python-%EB%B9%84%EC%9C%A8%EC%9D%84-%EC%9C%A0%EC%A7%80%ED%95%98%EB%A9%B4%EC%84%9C-%EC%88%AB%EC%9E%90-%EB%B2%94%EC%9C%84%EB%A5%BC-%EB%8B%A4%EB%A5%B8-%EB%B2%94%EC%9C%84%EB%A1%9C-%EB%B3%80%ED%99%98/
    return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax - outMin))


print(num_to_range(5, 0, 10, 0, 100))  # 50.0
