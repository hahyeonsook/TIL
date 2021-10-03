while True:
    lines = sorted(list(map(int, input().split())))

    if sum(lines) == 0:
        break
    a, b, m = lines
    if m ** 2 == (a ** 2 + b ** 2):
        print("right")
    else:
        print("wrong")
