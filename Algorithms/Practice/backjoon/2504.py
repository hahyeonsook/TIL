# REF https://www.acmicpc.net/problem/2504
# 1초, 20,000,000

# (), []의 짝이 맞으면 올바른 괄호열이다.
# 올바른 괄호열의 경우 괄호열의 값을 아래와 같이 정의할 때, 괄호열의 값을 구하라.
# 1. () = 2
# 2. [] = 3
# 3. (x) = 2*x
# 4. [x] = 3*x
# 5. 올바른 괄호열인 x, y일 때 xy = x+y

# 입력
# 괄호열을 나타내는 문자열이 주어짐. 1 <= len(문자열) <= 30

# 출력
# 괄호열의 값을 나타내는 정수
# 올바르지 않은 괄호열이면 0을 출력


from collections import deque


def solution(string):
    answer = 0
    lst = deque()

    for char in string:
        if char in "([":
            lst.appendleft(char)

        else:
            outside_paren = ")" if char == "(" else "]"
            while lst[0] != outside_paren:
                lst.pop()
