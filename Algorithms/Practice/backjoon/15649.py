def solution(N, M):
    def choice(sequences, sub, choiced):
        if len(sub) == M:
            sequences.append(" ".join(map(str, sub)))
            return sequences, sub

        for n in range(N):
            if not choiced[n]:
                sub.append(n + 1)
                choiced[n] = True
                sequences, sub = choice(sequences, sub, choiced)
                sub.pop()
                choiced[n] = False

        return sequences, sub

    sequences, _ = choice([], [], [False] * N)
    return "\n".join(sequences)


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
