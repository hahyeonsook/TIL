# REF https://www.30secondsofcode.org/python/s/find-keys
# 주어진 dict에서 지정된 val을 가진 모든 키를 찾아라.


def find_keys(dict, val):
    return list(key for key, value in dict.items() if value == val)


ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 10,
}
print(find_keys(ages, 10))  # [ 'Peter', 'Anna' ]

# REF https://www.30secondsofcode.org/python/s/camel
# 문자열을 카멜형식으로 바꿔라.

from re import sub


def camel(s):
    #        _ or -를 ' ' 공백으로 변환한 후 title()
    #                          title(): 공백을 기준으로 맨 앞의 문자를 대문자로 변환
    #                                  모든 공백을 없앰
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    # 맨 앞글자는 소문자
    # return s[0].lower() + s[1:] # 이렇게 해도 값은 같음. 버전별로 달라서 다르게 해놓은 걸까
    return "".join([s[0].lower(), s[1:]])


print(camel("some_database_field_name"))  # 'someDatabaseFieldName'
print(camel("Some label that needs to be camelized"))
# 'someLabelThatNeedsToBeCamelized'
print(camel("some-javascript-property"))  # 'someJavascriptProperty'
print(camel("some-mixed_string with spaces_underscores-and-hyphens"))
# 'someMixedStringWithSpacesUnderscoresAndHyphens'

# REF https://www.30secondsofcode.org/python/s/words
# 주어진 문자열을 단어의 리스트로 변환하라.
# 패턴이 주어지면, 해당 패턴으로 단어를 구분하라.

import re


def words(s, pattern="[a-zA-Z-]+"):
    # finditer(): 정규식과 매치되는 모든 문자열을 리스트로 리턴
    return re.findall(pattern, s)


print(words("I love Python!!"))  # ['I', 'love', 'Python']
print(words("python, javaScript & coffee"))  # ['python', 'javaScript', 'coffee']
#                                      \b = boundary
print(words("build -q --out one-item", r"\b[a-zA-Z-]+\b"))
# ['build', 'q', 'out', 'one-item']
