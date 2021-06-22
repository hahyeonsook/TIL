# REF https://www.30secondsofcode.org/python/s/days-diff
# 주어진 두 날짜 사이의 일자 차이를 반환
def days_diff(start, end):
    # datetime 의 date 클래스를 빼기 연산하면 datetime.timedelta 클래스가 반환
    # timedela.days는 timedelta의 일수 값을 반환.
    return (end - start).days


from datetime import date, datetime

print(days_diff(date(2020, 10, 25), date(2020, 10, 28)))  # 3

# REF https://www.30secondsofcode.org/python/s/average
# 두 개 이상의 숫자의 평균값을 반환
def average(*args):
    # sum의 두 번째 인자는 시작 값을 나타내는데, 0.0부터 더해줌으로써 int 값이 아닌 float 값이 되게 함.
    # sum([1, 2, 3]) # 6
    # sum([1, 2, 3]) # 6.0
    return sum(args, 0.0) / len(args)


print(average(*[1, 2, 3]))  # 2.0
print(average(1, 2, 3))  # 2.0


# REF https://www.30secondsofcode.org/python/s/add-days
# 주어진 날짜로부터 n 일 이후의 날짜를 반환
from datetime import timedelta, datetime


def add_days(n, d=datetime.today()):
    return d + timedelta(n)


from datetime import date

print(add_days(5, date(2020, 10, 25)))  # date(2020, 10, 30)
print(add_days(-5, date(2020, 10, 25)))  # date(2020, 10, 20)


# REF https://www.30secondsofcode.org/python/s/palindrome
# 회문: 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장
# 지정된 문자열이 회문인지 반환
from re import sub


def palindrome(s):
    # sub(A, B, C)
    # C에서 A를 찾아 B로 바꿈.
    # A는 정규 표현식으로 검색 패턴을 지정할 수 있음.
    # [xy] : x와 y중 하나
    # \W : non word 알파벳 and 숫자 and _가 아닌 문자
    s = sub("[\W_]", "", s.lower())
    return s == s[::-1]


print(palindrome("taco cat"))  # True
