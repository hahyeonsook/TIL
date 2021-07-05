# REF https://www.30secondsofcode.org/python/s/includes-all
# `values` 안의 모든 값이 `lst` 안에 포함되는지 검사하라.


def includes_all(lst, values):
    for v in values:
        if v not in values:
            return False
    return True


print(includes_all([1, 2, 3, 4], [1, 4]))  # True
print(includes_all([1, 2, 3, 4], [1, 5]))  # False


# REF https://www.30secondsofcode.org/python/s/curry
# 함수를 쿼리하라.
# `functools.partial()`을 사용하여 `args`가 부분적으로 적용된 상태에서 `fn` 처럼 동작하는 객체를 return 하라.

from functools import partial


def curry(fn, *args):
    # 호출될 때 args와 keywords로 호출된 func처럼 동작하는 새 partial 객체를 반환
    return partial(fn, *args)


add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20)  # 30

# REF https://www.30secondsofcode.org/python/s/compose-right
# 왼쪽 함수에 오른쪽 함수를 합성하라.
from functools import reduce


def compose_right(*fns):
    # reduce(func, iterable) : iterable한 값을 func에 차례로 수행한 후 단일 값으로 결과를 반환
    #                   왼, 오:              오(왼(args))
    return reduce(lambda f, g: lambda *args: g(f(*args)), fns)


add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
print(add_and_square(1, 2))  # 9


# REF https://www.30secondsofcode.org/python/s/compose
# 오른쪽 함수에 왼쪽 함수를 합성하라.

from functools import reduce


def compose(*fns):
    #                   왼, 오:              왼(오(args))
    return reduce(lambda f, g: lambda *args: f(g(*args)), fns)


add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
print(multiply_and_add_5(5, 2))  # 15
