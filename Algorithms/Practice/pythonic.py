a, b = map(int, input().split())
print(a, b)

# 입력받은 list에서 첫번째, 마지막 값을 제외
_list = [1, 2, 3, 4, 5]
# 가변인자, 인자의 개수가 몇 개가 될지 확실하지 않을때 사용
first_index, *rest, last_index = _list
print(rest)

_list = [1, 2, 3, 4, 5]
for num in _list:
    print(num, end=" ")  # 1 2 3 4 5

_list = [1, 2, 3, 4, 5]
# Unpacking, 컨테이너형 구조(list, 튜플, set)에선 모두 적용할 수 있다.
print(*_list)

a, b, c = [1, 2, 3]
# Packing, 하나의 변수에 여러 값을 할당하면 튜플로 묶인다.
d = a, b, c
print(d)  # (1, 2, 3)

_list = [i for i in range(10)]  # 0 1 2 3 4 5 6 7 8 9

import sys

input = sys.stdin.readline

_ = input()
_set = set(map(int, input().split()))
q = input()
_list = list(map(int, input().split()))

print(*[1 if dt in _set else 0 for dt in _list], sep="\n")

square = [[x ** 2 for x in range(3)] for _ in range(3)]
print(square)  # [[1, 4, 9], [1, 4, 9], [1, 4, 9]]

# 오타
# 1 ~ 10을 담는 리스트를 만들어보자.
_list = [i + 1 for i in range(10)]

# 오타
# 2, 4, 5, ..., 20을 담는 리스트를 만들어보자.
_list = [(i + 1) * 2 for i in range(10)]

# 오타
# 주어진 리스트를 받아 3의 배수만 담는 리스트를 만들어보자.
import random

tmp = [random.randrange(1, 200) for i in range(100)]
# 뒤에 붙은 if는 값을 넣을지 뺄지를 결정하는 조건
_list = [i for i in tmp if tmp % 3 == 0]

# 값이 두개 들어있는 튜플을 받아 리스트를 생성하되, 튜플 내부의 값을 뒤집어서 저장하라.
list_of_tuple = [(i, j) for i in range(100) for j in range(100, 0, -1)]
_list = [(j, i) for i, j in list_of_tuple]

# 주어진 리스트를 그대로 담되, 15가 넘어가는 값은 15로 바꿔서 저장하라.
_list = [i if i <= 15 else 15 for i in tmp]

# 두 개의 리스트를 합치되, 가능한 모든 조합을 저장하는 리스트를 만들어라.
x = [i for i in range(5)]
y = [i for i in range(5)]
_list = [(i, j) for i in x for j in y]


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(100):
    # O(N)
    if i in data:
        print(i)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_data_set = set(data)
for i in range(100):
    # O(1)
    if i in _data_set:
        print(i)

i_want_to_erase_duplicate_element = [21, 31, 65, 21, 58, 94, 13, 31, 58]
complete_list = list(set(i_want_to_erase_duplicate_element))  # 21, 31, 65, 58, 94, 13

test_list = ["Test", "test", "TEST", "tteesstt"]
converted_list = list(
    set(map(lambda string: string.lower(), test_list))
)  # test, tteesstt

fruit = ["apple", "grape", "orange", "banana"]
price = [3200, 15200, 9800, 5000]
_dict = {}

for i in range(len(price)):
    _dict.append(
        (fruit[i], price[i])
    )  # {'apple' : 3200, 'grape' : 15200, 'orange' : 9000, 'banana' : 5000}

fruit = ["apple", "grape", "orange", "banana"]
price = [3200, 15200, 9800, 5000]
_dict = dict(zip(fruit, price))

print(_dict["strawberry"])  # Error!

fruit = ["apple", "grape", "orange", "banana"]
price = [3200, 15200, 9800, 5000]
_dict = dict(zip(fruit, price))

print(_dict.setdefault("strawberry", 0))  # 0

from collections import defaultdict

movie_review = [
    ("Train to Busan", 4),
    ("Clementine", 5),
    ("Parasite", 4.5),
    ("Train to Busan", 4.2),
    ("Train to Busan", 4.5),
    ("Clementine", 5),
]

# defaultdict(<class 'list'>, {})
index = defaultdict(list)

for review in movie_review:
    # 값을 검색할 때, 값이 없으면 인자로 넘겨준 값이 default 값이 된다.
    # review[0] 제목, review[1] 별점
    index[review[0]].append(
        review[1]
    )  # {'Train to Busan': [4, 4.2, 4.5], 'Clementine': [5, 5], 'Parasite': [4.5]}

# dict unpacking
fruit = ["apple", "grape", "orange", "banana"]
price = [3200, 15200, 9800, 5000]
_dict = dict(zip(fruit, price))

print(*_dict.keys())  # apple grape orange banana
print(*_dict.values())  # 3200 15200 9800 5000
print(
    *_dict.items()
)  # ('apple', 3200) ('grape', 15200) ('orange', 9800) ('banana', 5000)

_list = [5, 6, 4, 8, 2, 3]
sorted_list = sorted(_list)  # 2, 3, 4, 5, 6, 8
_list.sort()
print(_list)  # 2, 3, 4, 5, 6, 8

_set = {65, 12, 15, 156, 31, 54, 94, 82, 31}
# dict와 set은 순서가 없다.
_set.sort()  # Error!
print(sorted(_set))

_list = [5, 6, 4, 8, 2, 3]
sorted_list = sorted(_list, reverse=True)  # 8, 6, 5, 4, 3, 2

# 오타
_list = [(1, 3), (8, 2), (2, 5), (4, 7)]
# A custom key function can be supplied to customize the sort order
sorted_list = sorted(_list, key=lambda dt: dt[0])

_list = [(1, 3), (8, 2), (2, 5), (4, 7)]
# 각각의 값이 음수가 되면 대소관계가 반전되기 때문에, 음수로 변환해서 대소관계를 비교해서 정렬한다.
sorted_list = sorted(_list, key=lambda dt: (dt[0], -dt[1]))

_list = ["CHicken", "hamburger", "Sushi", "chocolate"]
print(sorted(_list))
# 문자열은 대소관계를 비교하기 때문에, 소문자로 바꾸면 대소관계 상관없이 정렬할 수 있다.
print(_list, key=lambda dt: dt.lower())

print("     asdasd     ".strip())  # asdasd
# 양 끝의 문자열을 제거하는 함수다. default 값이 ' '이다.
# 두 개이상의 문자열을 넣어주면 두 개를 모두 지운다. and 연산이 아닌 or 연산이다.
print("===chicken===".strip("="))  # chicken
print("==  =chicken=  ==".strip("= "))  # chicken

string = "I am Hungry..."
print(string[::-1])
# reversed(string) >>> <reversed object at 0x000001E5284E67F0>
# 메모리 주소만 나온다.
# for i in ~ 구조를 사용하거나 join을 사용한다.
print("".join(reversed(string)))


import itertools

_list = [1, 2, 3, 4]
# 모든 조합을 출력한다. 중복이 없고 순서를 구분하지 않는다.
iter = itertools.combinations(_list, 2)  # 12 13 14 23 24 34
# 순열을 출력한다. 중복이 없고 순서를 구분한다.
iter = itertools.permutations(_list, 2)  # 12 13 14 21 23 24 31 32 34 41 42 43
# 모든 조합을 출력한다. 중복이 가능하고, 순서를 구분하지 않는다.
iter = itertools.combinations_with_replacement(
    _list, 2
)  # 11 12 13 14 22 23 24 33 34 44
# 모든 가능한 경우의 수를 출력한다.
iter = itertools.product(_list, 2)  # 11 12 13 14 21 22 23 24 31 32 33 34 41 42 43 44

# join
# iterable의 문자열들을 이어 붙인 문자열을 돌려준다.
_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(", ".join(_list))

N = 10
sample = [[x for x in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if sample[i][j] != 1:
            break
    # loop를 진행하다가 else가 나오면, 반복문을 break로 탈출하지 않았다면 진입하는 구간으로 사용한다.
    else:
        print("Hello")

_list = ["a", "b", "c", "d", "e", "f", "g"]
# 목표: (1, a), (2, b), (3, c)...

for i in range(len(_list)):
    print(i, _list[i])

# (인덱스, 값) 현태의 튜플을 돌려준다.
for idx, val in enumerate(_list):
    print(idx, val)


def countLetters(word):
    counter = {}
    for letter in word:
        counter.setdefault(letter, 0)
        counter[letter] += 1
    return counter


countLetters(
    "Hello World"
)  # {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}


from collections import Counter

Counter(
    "hello world"
)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})


from collections import Counter

# most_common()은 전체 결과를 튜플의 리스트로 리턴하고, 숫자를 명시하면 상위 n개에 해당하는 결과만 출력한다.
Counter(
    "hello world"
).most_common()  # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
Counter("hello world").most_common(2)  # [('l', 3), ('o', 2)]
