if __name__ == "__main__":
    N = int(input().strip())
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    sidx, eidx = 1, 10
    while len(numbers) <= N:
        for number in numbers[sidx:eidx]:
            for next_number in range(int(number[-1])):
                numbers.append(number + str(next_number))
            if len(numbers) > N:
                break
        sidx, eidx = eidx, len(numbers)
        if len(numbers) >= 1023:
            break

    if len(numbers) <= N:
        print(-1)
    else:
        print(numbers[N])
