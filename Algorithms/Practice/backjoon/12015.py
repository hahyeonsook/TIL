import sys
import bisect


def solution(N):
    arr = list(map(int, input().split()))

    dp = [arr[0]]
    for i in range(N):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        # arr[i] <= dp[-1]
        else:
            # dp에 arr[i] 가 들어갈 위치를 선정
            # arr가 정렬되어 있다는 가정 하에 x 값이 들어갈 위치 반환
            idx = bisect.bisect_left(dp, arr[i])
            dp[idx] = min(dp[idx], arr[i])
    return len(dp)


# print(solution(int(input().strip())))

N = int(input().strip())
nums = list(map(int, input().split()))

dp = [nums[0]]
for idx in range(1, N):
    if nums[idx] > dp[-1]:
        dp.append(nums[idx])
    else:
        insert_idx = bisect.bisect_left(dp, nums[idx])
        dp[insert_idx] = nums[idx]
print(len(dp))
