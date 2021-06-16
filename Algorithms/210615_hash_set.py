_dict = dict(one=1, two=2, three=3)
_dict = {"one": 1, "two": 2, "three": 3}

_number = ["one", "two", "three", "four"]
_num = [1, 2, 3, 4]
_dict = dict(zip(_number, _num))

new_dict = {word: number for word, number in _dict.items() if number > 1}

# 딕셔너리 안에 키가 있으면 값을 출력하고, 없으면 값을 넣자.
print(_dict.setdefault(5, "Test"))

# dict의 서브 클래스로, 인자로 주어진 객체의 기본값을 딕셔너리의 초깃값으로 지정할 수 있음
# int, list, set 등으로 기본값 설정 가능
# 약간의 성능 저하가 존재함.
from collections import defaultdict

int_dict = defaultdict(int)
int_dict["asd"] += 1
print(int_dict)

_number = ["one", "two", "three", "four"]
_num = [1, 2, 3, 4]
_dict = dict(zip(_number, _num))

# dict를 key 값을 지정하지 않고 sorted 하면 기본적으로 키값을 기준으로 정렬하게 된다.
print(sorted(_dict))  # ['four', 'one', 'three', 'two']
print(sorted(_dict.items()))
# value 값으로 정렬하기
print(sorted(_dict.items(), key=lambda x: x[1]))


_set = set()
_list = [1, 2, 3, 4, 5, 6, 1, 2, 3]
_set = set(_list)

# 교집합
print(_set & {1, 2, 3})  # {1, 2, 3}
# python 3.9 에서는 + 연산자는 TypeError를 낸다.
# 합집합
print(_set | {10, 11, 12})  # {1, 2, 3, 4, 5, 6, 10, 11, 12}
# 차집합
print(_set - {1, 2, 3})  # {4, 5, 6}
# sorted는 list로 반환한다.
print(sorted(_set))  # [1, 2, 3, 4, 5, 6]
