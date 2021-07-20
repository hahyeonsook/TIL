# REF https://www.acmicpc.net/problem/21939
# 1초, 20,000,000
# 골드 4

# 코테 대비 문제를 뽑아 "문제 번호, 난이도"로 정리했다.
# recommend x, add P L, solved P 명령어를 수행하는 프로그램을 만들어라.

# 입력
# N, 문제의 개수
# N+1줄 까지, P L, 문제번호 난이도
# 1 <= N, P <= 100,000
# 1 <= L <= 100, 자연수
# N+2줄, M, 입력될 명령어의 개수
# 1 <= M <= 10,000
# M 줄, 명령문

# 출력
# 명령이 주어질 때마다 문제 번호를 한 줄씩 출력한다.

# 틀렸습니다.

import sys

input = sys.stdin.readline
output = sys.stdout.write

import heapq
import collections

solved_problems = collections.defaultdict(bool)
asc_problems = []
des_problems = []


def command(cmd):
    def recommend(cmd):
        tmp, x = cmd.split()
        x = int(x)

        problems = []
        if x > 0:
            max_problem = 0
            while True:
                problem = heapq.heappop(des_problems)
                if solved_problems[problem[1]]:
                    max_problem = max(max_problem, problem[1])
                    problems.append(problem)
                else:
                    continue
                if problem[1] != des_problems[0][1]:
                    break
            list(map(lambda x: heapq.heappush(des_problems, x), problems))
            print(max_problem)
        elif x < 0:
            min_problem = 100001
            while True:
                problem = heapq.heappop(asc_problems)
                if solved_problems[problem[1]]:
                    min_problem = min(min_problem, problem[1])
                    problems.append(problem)
                else:
                    continue
                if problem[1] != asc_problems[0][1]:
                    break
            list(map(lambda x: heapq.heappush(asc_problems, x), problems))
            print(min_problem)
        return True

    def add(cmd):
        tmp, p, l = cmd.split()
        p = int(p)
        l = int(l)

        heapq.heappush(asc_problems, (l, p))
        heapq.heappush(des_problems, (-l, p))
        solved_problems[p] = True
        return True

    def solved(cmd):
        tmp, p = cmd.split()
        p = int(p)
        solved_problems[p] = False

    if "recommend" in cmd:
        return recommend(cmd)
    elif "add" in cmd:
        return add(cmd)
    elif "solved" in cmd:
        return solved(cmd)


n = int(input().strip())
for _ in range(n):
    problem, rank = map(int, input().split())
    heapq.heappush(asc_problems, (rank, problem))
    heapq.heappush(des_problems, (-rank, problem))
    solved_problems[problem] = True
m = int(input().strip())
for _ in range(m):
    cmd = input().strip()
    if cmd == "":
        break
    command(cmd)
