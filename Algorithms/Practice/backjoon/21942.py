# REF https://acmicpc.net/problem/21942
# 1초, 20,000,000
# 골드 2

# 부품을 빌려갈 경우, 부품 대여장에 정보를 반드시 작성해야 한다.
# 부품을 반납할 경우, 부품 대여장에 정보를 반드시 작성해야 한다.
# 대여기간을 정하고, 대여기간을 넘길 경우 1분당 벌금을 부여하도록 한다.
# yyyy-MM-dd hh:mm [부품 이름] [동아리 회원 닉네임]
# 한 사람이 같은 종류의 부품을 두개 이상 대여하고 있는 상태일 수 없다.
# 한 사람이 같은 시각에 서로 다른 종류의 부품들을 대여하는 것이 가능하다.
# 같은 사람이더라도, 대여 기간은 부품마다 별도로 적용된다.

# N L F, 작성된 정보의 개수, 대여할 수 있는 기간, 벌금
#                           DDD/hh:mm,
# 2 <= N <= 80,000, N은 짝수
# 0 <= DDD <= 200
# 1 <= MM <= 12
# 0 <= hh <= 23 0 <= mm <= 59 1 <= F <= 4,000
# 5 <= |P|, |M| <= 20
# 부품을 반납하지 않은 사람은 없음
# N + 1줄, 시간순
# yyyy-MM-dd hh:mm P M, 시각 부품이름 회원

# 출력
# 벌금을 내야하는 사람들을 사전순으로 출력
# 닉네임 벌금
# 내야하는 사람이 없으면 -1을 출력

import sys, re

input = sys.stdin.readline
# 대여장 정보 라인 수, 최대 대여 기간, 1분당 벌금
N, L, F = input().split()

import heapq
from collections import defaultdict
from datetime import datetime, timedelta


def solution(N, L, F):
    default_date = datetime(2020, 12, 31, 0, 0)
    # 대여 리스트를 저장하는 dict, 2021년도부터 입력을 받기 때문에 2020 12 31로 초기화
    rental_dict = defaultdict(lambda: default_date)
    charge_lst = []
    for _ in range(N):
        # 입력받은 대여 정보를 뒤에서부터 파싱
        date, component, user = input().rsplit(maxsplit=2)
        # default_date가 아니면 부품을 반납하는 정보이므로 대여 기간을 계산
        if rental_dict[(user, component)] != default_date:
            # 저장되어 있는 datetime 값과 입력받은 datetime의 차이 계산
            delta = (
                datetime.strptime(date, "%Y-%m-%d %H:%M")
                - rental_dict[(user, component)]
            )
            # 차이가 최대 대여기간보다 크면 charge_lst에 heappush
            if delta > L:
                minutes = delta - L
                charge = F * ((minutes.days * (24 * 60)) + (minutes.seconds // 60))
                heapq.heappush(charge_lst, (user, charge))

            rental_dict[(user, component)] = default_date
        # default_date이면 부품을 대여하는 정보
        else:
            rental_dict[(user, component)] = datetime.strptime(date, "%Y-%m-%d %H:%M")

    if not charge_lst:
        print(-1)

    while charge_lst:
        user, charge = heapq.heappop(charge_lst)
        while charge_lst and user == charge_lst[0][0]:
            u, c = heapq.heappop(charge_lst)
            charge += c
        print(user, charge)


N, F = int(N), int(F)
d, h, m = map(int, re.split("[:/]", L))
L = timedelta(days=d, hours=h, minutes=m)
solution(N, L, F)
