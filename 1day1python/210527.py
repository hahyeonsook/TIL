# REF https://www.30secondsofcode.org/python/s/all-unique
# 중복 값이 없는지 반환.
def all_unique(lst):
    # set은 중복 값을 없애줌.
    return len(lst) == len(set(lst))


x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 2, 2, 4, 5, 6, 7]

print(all_unique(x))  # True
print(all_unique(y))  # False

# REF https://www.30secondsofcode.org/python/s/capitalize-every-word
# 첫 글자를 대문자로 변경.
def capitalize_every_word(s):
    # 문자열 데이터에서 title() 메소드를 실행시키면 문자열의 첫 글자를 대문자로 변경함.
    # 한글은 변경없음.
    return s.title()


print(capitalize_every_word("hello world!"))  # Hello World!
print(capitalize_every_word("안녕 세계!"))  # 안녕 세계!
