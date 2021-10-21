from copy import deepcopy


def solution(rows, columns, queries):
    answer = []

    # 맵 초기화
    maps = [[(r * columns) + c for c in range(1, columns + 1)] for r in range(rows)]

    def rotate(x1, y1, x2, y2):
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        vals = [maps[x1][y1]]

        # 상우
        temp = maps[x1][y1]
        for y in range(y1 + 1, y2 + 1):
            maps[x1][y], temp = temp, maps[x1][y]
            vals.append(temp)
        # 우하
        for x in range(x1 + 1, x2 + 1):
            maps[x][y2], temp = temp, maps[x][y2]
            vals.append(temp)
        # 하좌
        for y in range(y2 - 1, y1 - 1, -1):
            maps[x2][y], temp = temp, maps[x2][y]
            vals.append(temp)
        # 좌상
        for x in range(x2 - 1, x1 - 1, -1):
            maps[x][y1], temp = temp, maps[x][y1]
            vals.append(temp)

        return min(vals)

    for x1, y1, x2, y2 in queries:
        answer.append(rotate(x1, y1, x2, y2))
    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
