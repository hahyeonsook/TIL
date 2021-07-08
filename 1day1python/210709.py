# REF https://www.30secondsofcode.org/python/s/check-prop
# 주어진 객체의 속성을 주어진 함수에 적용하는 함수를 생성하라.
def check_prop(fn, prop):
    return lambda obj: fn(obj[prop])


check_age = check_prop(lambda x: x >= 18, "age")
user = {"name": "Mark", "age": 18}
print(check_age(user))  # True

# REF https://www.30secondsofcode.org/python/s/none
# 주어진 함수가 리스트의 요소에 대해 하나 이상이 True를 반환하는지 확인하라.
def none(lst, fn=lambda x: x):
    # all() :  모든 요소가 참이거나 비어있으면 True, 그 외의 경우에는 False
    return all(not fn(x) for x in lst)


print(none([0, 1, 2, 0], lambda x: x >= 2))  # False
print(none([0, 0, 0]))  # True
