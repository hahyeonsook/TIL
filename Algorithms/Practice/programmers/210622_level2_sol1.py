# 1과 0으로 채워진 board가 있음.
# 표에서 1로 이뤄진 가장 큰 정사각형을 찾아 넓이를 return하라.
# 단, 축은 평행해야 한다.

# 입력
# 2차원 배열

# 출력
# int


def solution(board):
    from collections import Counter

    answer = 0
    n = len(board)
    inversed = list(map(list, zip(*board)))
    rows = [0 for _ in range(n)]
    columns = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
        board[][]

    return answer


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
