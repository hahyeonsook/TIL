# REF https://www.30secondsofcode.org/python/s/byte-size
# 문자의 바이트 길이를 반환
def byte_size(s):
    return len(s.encode("utf-8"))


print(byte_size("😀"))  # 4
print(byte_size("Hello World"))  # 11

# REF https://www.30secondsofcode.org/python/s/pad-number
# 주어진 숫자를 주어진 길이로 패딩하여 반환
def pad_number(n, l):
    # 문자열 앞에 공백을 채우는 함수
    # return str(n).rjust(l)
    # 문자열 앞에 0을 채우는 함수
    return str(n).zfill(l)


print(pad_number(1234, 6))


# REF https://www.30secondsofcode.org/python/s/clamp-number
# 주어진 num 이 범위 안에 있는지
# 범위 안에 있다면 num을 출력하고, 없으면 범위에서 가장 가까운 범위 숫자를 반환
def clamp_number(num, a, b):
    # max: 가장 큰 값을 반환함
    # min: 가장 작은 값을 반환함
    # min(a, b) < num < max(a, b)
    # min(num, max(a, b)) == num -> num은 범위 안
    # max(num, min(a, b)) == num -> num은 범위 안
    # 위의 두개를 합친 것임
    #          min(num, max(a, b)) 범위 안이면 num이 return
    #      max(num,                 min(a, b)) 범위 안이면 num이 return
    return max(min(num, max(a, b)), min(a, b))


print(clamp_number(2, 3, 5))  # 3
# num이 범위가 아닐 경우는
# num > max(a, b) or num < min(a, b)
# min(num, max(a, b)) == max(a, b) -> num이 범위 밖, num이 범위보다 큼 => max(a, b)가 num과 더 가까운 값, return 값
# max(num, min(a, b)) == min(a, b) -> num이 범위 밖, num이 범위보다 작음 => min(a, b)가 num과 더 가까운 값, return 값
#      min(num, max(a, b) == max(a, b), num이 범위보다 큼, max(a, b)를 구해야 함.
# max( max(a, b),          min(a, b)) <- max(a, b)를 구함.
# max(num,                 min(a, b)) == min(a, b), num이 범위보다 작음, min(a, b)를 구해야 함. <- min(a, b)를 구함.
# max(min(num, max(a, b)), min(a, b))
print(clamp_number(1, -1, -5))  # -1


# REF https://www.30secondsofcode.org/python/s/all-equal
# 리스트의 모든 값이 같은지 반환
def all_equal(lst):
    return len(set(lst)) == 1


print(all_equal([1, 2, 3, 4, 5, 6]))  # False
print(all_equal([1, 1, 1, 1]))  # True
