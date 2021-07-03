# 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 한다.
# 많이 재생된 장르에 속한 노래를 먼저 수록한다.
# 장르 내에서 많이 재생된 노래를 먼저 수록한다.
# 장르 내에서 재생 횟수가 같다면, 고유 번호가 낮은 노래를 먼저 수록한다.
# 장르별, 재생된 횟수별, 고유 번호별 정렬
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하라.

# genres[i]는 고유 번호가 i인 노래의 장르이다.
# plays[i]는 고유 번호가 i인 노래의 재생된 횟수
# 1 <= len(genres), len(plays) <= 10,000
# 장르 종류는 100개 미만
# 장르에 속한 곡이 하나면, 하나의 곡만 선택
# 모든 장르는 재생된 횟수가 다르다.

import collections


def solution(genres, plays):
    answer = []
    # 장르별 플레이 횟수 구하기
    genres_hash = collections.defaultdict(int)
    for i in range(len(plays)):
        genres_hash[genres[i]] += plays[i]

    songs_hash = {
        index: (genres_hash[info[0]], info[1])
        for index, info in enumerate(list(zip(genres, plays)))
    }
    songs_rank = sorted(
        songs_hash.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True
    )

    for i in range(len(songs_rank)):
        genre = 0
        while genre < 2:
            if songs_rank[i - 1][1][0] == songs_rank[i][1][0]:
                answer.append(songs_rank[i][0])

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
