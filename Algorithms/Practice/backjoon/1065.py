def ok(number):
    number = list(map(int, str(number)))
    if len(number) == 1:
        return True

    step = number[1] - number[0]
    for idx in range(1, len(number)):
        if number[idx - 1] + step != number[idx]:
            return False
    return True


if __name__ == "__main__":
    N = int(input().strip())

    count = 0
    for num in range(1, N + 1):
        if ok(num):
            count += 1
    print(count)
