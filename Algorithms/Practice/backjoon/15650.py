def solution(N, M):
    def choice(sequences, sub):
        if len(sub) == M:
            sequences.append(" ".join(map(str, sub)))
            return sequences, sub
        for n in range(sub[-1], N):
            sub.append(n + 1)
            sequences, sub = choice(sequences, sub)
            sub.pop()
        return sequences, sub

    sequences = []
    for n in range(N):
        seq, _ = choice([], [n + 1])
        sequences.extend(seq)

    return "\n".join(sequences)


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
