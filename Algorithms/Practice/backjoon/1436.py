def solution(N):
    numbers = set([666])

    # 최대 9자리 숫자
    for b in range(1, 7):
        blank = list(map(str, range(10 ** b)))
        for idx in range(b + 1):
            for blank_number in blank:
                blank_number = blank_number.zfill(b)
                numbers.add(int(blank_number[idx:] + "666" + blank_number[:idx]))

        if len(numbers) >= N:
            return sorted(numbers)[N - 1]


if __name__ == "__main__":
    print(solution(int(input().strip())))
