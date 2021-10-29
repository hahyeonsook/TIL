def solution(N, M):

    robot = list(map(int, input().split()))
    maps = [list(map(int, input().split())) for _ in range(N)]
    cleaned = [[False for _ in range(M)] for _ in range(N)]

    if robot[-1] % 2 != 0:
        robot[-1] = (robot[-1] + 2) % 4

    #         북 서 남 동
    dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]

    def dfs(vr, vc, vd):
        cleaned[vr][vc] = True

        # 현재 방향을 기준으로 왼쪽 방향부터 탐색
        for d in range(1, 5):
            wr, wc = vr + dr[(d + vd) % 4], vc + dc[(d + vd) % 4]
            # 벽이 아니고, 청소하지 않은 공간이 존재하면, 1번부터 진행.
            if -1 < wr < N and -1 < wc < M and not maps[wr][wc] and not cleaned[wr][wc]:
                if dfs(wr, wc, (d + vd) % 4):
                    return True

        # 네 방향 모두 청소가 되어 있거나, 벽인 경우에는,
        # 바라보는 방향을 유지한 채로 한 칸 후진하고 2번으로.
        wr, wc = vr - dr[vd], vc - dc[vd]
        if -1 < wr < N and -1 < wc < M and not maps[wr][wc]:
            if dfs(wr, wc, vd):
                return True

        # 한 칸 후진할 수 없다면, 작동을 멈춤.
        return True

    dfs(*robot)
    return sum(map(sum, cleaned))


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
