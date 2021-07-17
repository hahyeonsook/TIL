# REF https://www.acmicpc.net/problem/1620
# 2초, 40,000,000
# 실버 4

# 포켓몬 도감을 완성하라.
# 포켓몬의 이름을 보면 포켓몬의 번호를 말하고, 번호를 보면 이름을 말하라.

# 입력
# N M, 포켓몬의 개수 문제의 개수, 1 <= N, M <= 100,000
# 포켓몬의 이름은 모두 영어, 첫 글자만 대문자, 최대 길이는 20

import sys
import collections

input = sys.stdin.readline


def solution(n, m):
    results = []
    pocketmon_name = collections.defaultdict(str)
    pocketmon_number = collections.defaultdict(int)
    for index in range(1, n + 1):
        pocketmon = input().strip()
        pocketmon_name[index] = pocketmon
        pocketmon_number[pocketmon] = index

    for _ in range(m):
        test = input().strip()
        if test.isdigit():
            results.append(pocketmon_name[int(test)])
        else:
            results.append(pocketmon_number[test])
    return results


pocketmon_lst = [
    "Bulbasaur",
    "Ivysaur",
    "Venusaur",
    "Charmander",
    "Charmeleon",
    "Charizard",
    "Squirtle",
    "Wartortle",
    "Blastoise",
    "Caterpie",
    "Metapod",
    "Butterfree",
    "Weedle",
    "Kakuna",
    "Beedrill",
    "Pidgey",
    "Pidgeotto",
    "Pidgeot",
    "Rattata",
    "Raticate",
    "Spearow",
    "Fearow",
    "Ekans",
    "Arbok",
    "Pikachu",
    "Raichu",
]
test_lst = [
    "25",
    "Raichu",
    "3",
    "Pidgey",
    "Kakuna",
]
n, m = map(int, input().split())
print("\n".join(map(str, solution(n, m))))

import sys

input = sys.stdin.readline
import collections

n, m = map(int, input().split())
