# 34576kb 948ms
def solution(N):
    dic = sorted(set([input().strip() for _ in range(N)]), key=lambda s: (len(s), s))
    return "\n".join(dic)


# 34576kb 1112ms
def solution():
    N = int(input().strip())
    print(
        "\n".join(
            sorted(set([input().strip() for _ in range(N)]), key=lambda s: (len(s), s))
        )
    )


if __name__ == "__main__":
    print(solution(int(input().strip())))
