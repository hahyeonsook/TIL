import bisect


def solution(N):
    answer = []

    mid = 0
    sequence = []
    for idx in range(1, N + 1):
        number = int(input().strip())

        bisect.insort_left(sequence, number)
        if idx % 2 != 0 and mid + 1 < len(sequence):
            mid += 1
        answer.append(sequence[mid])
    return "\n".join(answer)


if __name__ == "__main__":
    print(solution(int(input().strip())))
