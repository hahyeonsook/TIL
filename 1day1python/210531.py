# REF https://www.30secondsofcode.org/python/s/every-nth
# 리스트의 모든 n번째 값을 반환.
def every_nth(lst, nth):
    # 인덱스 증가폭 지정하여 범위 내에서 인덱스 건너뛰며 가져올 수 있음.
    # [시작 인덱스:끝 인덱스:인덱스 증가폭]
    # 인덱스 증가폭을 음수로 지정하면, 요소를 뒤에서부터 가져올 수 있음.
    # [오른쪽에서 부터의 시작 인덱스: 오른쪽에서 부터의 시작 인덱스: 음수 증가폭]
    # >>> a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    # >>> a[5:1:-1]
    # [50, 40, 30, 20]
    return lst[nth - 1 :: nth]


print(every_nth([1, 2, 3, 4, 5, 6], 2))  # [2, 4, 6]

# REF
# 화씨 온도(물이 어는 온도 32도)에서 섭씨 온도(물이 어는 온도 0도)로 변환.
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8


print(fahrenheit_to_celsius(77))  # 25.0

# REF
# 해시 가능한 객체를 세기 위한 dict 서브 클래스
# 요소가 딕셔너리 키로 저장되고 개수가 딕셔너리 값으로 저장되는 컬렉션
from collections import Counter

# 리스트에서 고유하지 않은 값을 필터링.
def filter_non_unique(lst):
    return [item for item, count in Counter(lst).items() if count == 1]


print(filter_non_unique([1, 2, 2, 3, 4, 4, 5]))  # [1, 3, 5]

# REF https://www.30secondsofcode.org/python/s/for-each
# 리스트의 모든 값으로 주어진 함수를 실행.
# python에서 함수는 1급 객체이기 때문에 매개변수로 전달할 수 있음.
def for_each(itr, fn):
    for el in itr:
        fn(el)


for_each([1, 2, 3], print)  # 1 2 3
