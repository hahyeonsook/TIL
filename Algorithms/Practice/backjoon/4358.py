# REF https://www.acmicpc.net/problem/4358
# 1초, 20,000,000
# 골드 5

# 미국 전역의 나무들이 주어졌을 때, 각 종이 전체에서 몇 %를 차지하는지 구하는 프로그램을 만들어라.

# 입력
# 한 줄에 하나의 나무 종 이름이 주어진다.
# len(종) <= 10,000
# len(나무) <= 1,000,000

# 출력
# 주어진 각 종의 이름을 사전순으로 출력하고 비율을 백분율로 소수점 4째자리까지 반올림하여 출력하라.

import sys

input = sys.stdin.readline

import collections

trees = collections.Counter()
count = 0

while True:
    tree = input().strip()
    if tree == "":
        break
    trees[tree] += 1
    count += 1
sol = [
    "Ash 13.7931",
    "Aspen 3.4483",
    "Basswood 3.4483",
    "Beech 3.4483",
    "Black Walnut 3.4483",
    "Cherry 3.4483",
    "Cottonwood 3.4483",
    "Cypress 3.4483",
    "Gum 3.4483",
    "Hackberry 3.4483",
    "Hard Maple 3.4483",
    "Hickory 3.4483",
    "Pecan 3.4483",
    "Poplan 3.4483",
    "Red Alder 3.4483",
    "Red Elm 3.4483",
    "Red Oak 6.8966",
    "Sassafras 3.4483",
    "Soft Maple 3.4483",
    "Sycamore 3.4483",
    "White Oak 10.3448",
    "Willow 3.4483",
    "Yellow Birch 3.4483",
]
for index, tree in enumerate(sorted(trees)):
    percentage = round((trees[tree] / count) * 100, 4)
    print(f"{tree} {percentage:0.4f}")
