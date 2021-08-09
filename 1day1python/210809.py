# REF https://www.30secondsofcode.org/python/s/kebab
# 주어진 문자열을 kebab case로 변환하라.
# 케밥 케이스-하이픈으로 단어를 연결하는 표기법
from re import sub
import re


def kebab(s):
    return "-".join(
        # r"(\s|_|-)+"에 해당되는 패턴을 공백으로 변환
        sub(
            r"(\s|_|-)+",
            " ",
            sub(
                # *, +, ? 을 사용하여 반복적인 패턴을 찾는 것이 가능하나 반복의 횟수 제한은 불가
                # 패턴 뒤에 위치하는 중괄호에 숫자를 명시하면 해당 숫자만큼의 반복인 경우에만 매칭
                # REF https://www.geeksforgeeks.org/python-regex-lookahead/
                # ?=<lookahead_regex> : 현재 위치의 오른쪽에서 패턴이 일치하는지 assertion
                r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
                # group(): match Object의 메서드, 일치된 문자열을 반환한다.
                # group(0): 정규 표현식에서 ()는 그룹을 의미한다.
                # 이렇게 분리된 그룹들은 MatchObject의 group() 메서드에서 그룹 번호를 파라미터로 넣어 값을 가져올 수 있는데
                # 전체 전화번호를 가져올 때는 group() 혹은 group(0)을 사용한다.
                lambda mo: " " + mo.group(0).lower(),
                s,
            ),
        ).split()
    )


kebab("camelCase")  # 'camel-case'
kebab("some text")  # 'some-text'
kebab("some-mixed_string With spaces_underscores-and-hyphens")
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
kebab("AllThe-small Things")  # 'all-the-small-things'

# REF https://www.30secondsofcode.org/python/s/frequencies
from collections import defaultdict


def frequencies(lst):
    freq = defaultdict(int)
    for val in lst:
        freq[val] += 1
    return freq


print(frequencies(["a", "b", "a", "c", "a", "a", "b"]))  # { 'a': 4, 'b': 2, 'c': 1 }
