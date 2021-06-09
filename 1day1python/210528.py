# 섭씨 온도(물이 어는 온도 0도)를 화씨 온도(물이 어는 온도 32도)로 변환.
def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32


print(celsius_to_fahrenheit(180))  # 356.0


# REF https://www.30secondsofcode.org/python/s/compact
# falsey(False, None, 0, and "") value 제거.
def compact(lst):
    # 함수부분에 None을 넣으면 falsey values를 제거할 수 있음.
    # filter은 결과로 filter object를 리턴함. type(filter(func, value)) => <class 'type'>
    return list(filter(None, lst))


print(compact([0, 1, False, 2, "", 3, "a", "s", 34]))  # [1, 2, 3, 'a', 's', 34]

# REF https://www.30secondsofcode.org/python/s/count-occurrences
# list에서 주어진 값이 몇 개 있는지 반환
def count_occurrences(lst, val):
    # [val for val in list if 조건문]
    # ==와 and를 is로 대체할 수 있지않을까 생각했지만, is는 id 값을 비교하는 것이므로
    # list와 같은 가변 객체일 경우 값과 타입이 같아도 다르게 나올 수 있으므로 안됨.
    return len([x for x in lst if x == val and type(x) == type(val)])


print(count_occurrences([1, 1, 2, 3, 1], 1))  # 3

# REF https://www.30secondsofcode.org/python/s/rads-to-degrees
from math import pi

# degree(일반적으로 쓰이는 각의 단위, 몇 도)에서 radian(호의 길이가 반지름과 같게 되는 각이 1 라디안, 약 57.3도)으로 변환(각의 단위 변환).
def degrees_to_rads(deg):
    # pi radian = 180 degree
    # 1 radian = 180 / pi degree
    # x radian = x * 180 / pi degree
    return (deg * pi) / 180


print(degrees_to_rads(180))  # 3.141592653589793
