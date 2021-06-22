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
    print(phone_book)
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
