def solution():
    N = int(input().strip())
    cranes = sorted(list(map(int, input().split())), reverse=True)
    M = int(input().strip())
    boxes = sorted(list(map(int, input().split())), reverse=True)

    if boxes[0] > cranes[0]:
        return -1

    ans = 0
    while boxes:
        ans += 1
        for crane in cranes:
            for idx in range(len(boxes)):
                if boxes[idx] <= crane:
                    del boxes[idx]
                    break

    return ans


# https://www.acmicpc.net/source/34016535
def solution():
    N = int(input().strip())
    cranes = sorted(list(map(int, input().split())), reverse=True)
    M = int(input().strip())
    boxes = sorted(list(map(int, input().split())), reverse=True)

    if boxes[0] > cranes[0]:
        return -1

    cnt = [0] * N
    for box in boxes:
        idx = 0
        for j in range(N):
            if box <= cranes[j] and cnt[idx] > cnt[j]:
                idx = j
            elif box > cranes[j]:
                break
        cnt[idx] += 1
    return max(cnt)


if __name__ == "__main__":
    print(solution())
