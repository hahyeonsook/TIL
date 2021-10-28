if __name__ == "__main__":
    C = int(input().strip())

    for _ in range(C):
        score = list(map(int, input().strip().split()))
        N, score = score[0], score[1:]

        avg = sum(score) / N
        top = [s for s in score if s > avg]

        answer = str(round((len(top) / N) * 100, 3))
        zero = 3 - len(answer[answer.find(".") + 1 :])

        print(answer + "0" * zero + "%")
