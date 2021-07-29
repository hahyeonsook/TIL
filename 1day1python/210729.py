# REF https://www.30secondsofcode.org/python/s/capitalize
# 문자열의 첫 글자를 대문자로 바꿔라.
def capitalize(s, lower_rest=False):
    #               ['f'.upper(), 'ooBar']
    return "".join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])


print(capitalize("fooBar"))  # 'FooBar'
print(capitalize("fooBar", True))  # 'Foobar'

# REF https://www.30secondsofcode.org/python/s/snake
# 문자열을 snake case로 변환하라.
from re import sub


def snake(s):
    # sub(pattern, replace, str, ...): 정규식과 매치되면 replace로 변경
    # 정규 표현식
    #    (): 패턴의 요소를 하나로 묶어서 처리할 수 있도록 함.
    #    []: 가능한 문자열의 집합과 일치시킴
    #    + : 1회 이상 발생
    #                     \n: 일치하는 n번째 패턴
    return "_".join(  # _로 연결함.
        sub(
            "([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", s.replace("-", " "))
        ).split()  # split해서 공백으로 나눔.
    ).lower()  # 모든 문자를 소문자로 바꿈.


print(snake("camelCase"))  # 'camel_case'
print(snake("some text"))  # 'some_text'
print(snake("some-mixed_string With spaces_underscores-and-hyphens"))
# 'some_mixed_string_with_spaces_underscores_and_hyphens'
print(snake("AllThe-small Things"))  # 'all_the_small_things'


# REF https://www.30secondsofcode.org/python/s/initialize-2-d-list
# 주어진 가로, 세로의 크기만큼 val 값 으로 2차원 리스트를 초기화하라.
def initialize_2d_list(w, h, val=None):
    return [[val for x in range(w)] for y in range(h)]


print(initialize_2d_list(2, 2, 0))  # [[0, 0], [0, 0]]
