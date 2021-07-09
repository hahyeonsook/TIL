def solution(t, lst):
    def _gcd(a, b):
        if b == 0:
            return a
        if a % b == 0:
            return b
        else:
            return _gcd(b, a % b)

    for _ in range(t):
        a, b = map(int, lst[_].split())
        if a < b:
            a, b = b, a
        print((a * b // _gcd(a, b)))


lst = [
    "1 45000",
    "6 10",
    "13 17",
]
solution(3, lst)
