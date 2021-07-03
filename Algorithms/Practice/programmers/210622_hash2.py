# 전화번호부의 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인

# 입력
# 전화번호부 배열
# 1 <= phon_book <= 1,000,000
# 1 <= phon_number <= 20
# 번호 중복 없음

# 출력
# 접두어인 경우가 있다면 false, 없다면 true


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))


# 정확성: 83.3
# 효율성: 16.7
"""
테스트 1 〉	통과 (3.27ms, 10.9MB)
테스트 2 〉	통과 (3.03ms, 10.9MB)
테스트 3 〉	통과 (112.72ms, 30.6MB)
테스트 4 〉	통과 (118.43ms, 28.1MB)
"""

# 해시로 풀기
def solution(phone_book):
    phone_hash = {phone: 1 for phone in phone_book}

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in phone_hash and temp != phone_number:
                return False

    return True


def solution(phone_book):
    phone_hash = {phone: 1 for phone in phone_book}

    for phone_number in phone_book:
        for i in range(1, len(phone_number) + 1):
            if phone_number[:i] in phone_hash and phone_number[:i] != phone_number:
                return False
    return True


# 정확성: 83.3
# 효율성: 16.7
