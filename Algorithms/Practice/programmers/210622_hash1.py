import time

start = time.time()  # 시작 시간 저장


def solution(participant, completion):
    from collections import Counter

    if set(participant) != set(completion):
        return list(set(participant) - set(completion))[0]

    return Counter(participant).most_common(1)[0][0]


print(
    solution(
        ["mislav", "stanko", "mislav", "ana"],
        ["stanko", "mislav", "ana"],
    )
)

print(solution(["leo"], []))
print(solution(["leo", "leo"], ["leo"]))

# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	실패 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.20ms, 10.3MB)
테스트 4 〉	통과 (0.32ms, 10.4MB)
테스트 5 〉	실패 (0.44ms, 10.5MB)
효율성  테스트
테스트 1 〉	통과 (17.31ms, 21.7MB)
테스트 2 〉	통과 (27.02ms, 25.3MB)
테스트 3 〉	통과 (47.62ms, 33.6MB)
테스트 4 〉	통과 (47.85ms, 34.8MB)
테스트 5 〉	실패 (48.82ms, 34.8MB)
채점 결과
정확성: 30.0
효율성: 40.0
합계: 70.0 / 100.0
"""

from collections import Counter


def solution(participant, completion):
    return list(Counter(participant) - Counter(completion))[0]


print(
    solution(
        ["mislav", "stanko", "mislav", "ana"],
        ["stanko", "mislav", "ana"],
    )
)
