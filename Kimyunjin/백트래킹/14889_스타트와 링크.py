from itertools import combinations
import sys

n = int(input())    # n은 짝수
table = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
teams = combinations(range(n), n//2)     # 가능한 팀 조합
res = sys.maxsize   # 최대 정수

for team in teams:
    start_t = set(team)
    link_t = list(set(range(n)) - start_t)
    start_t = list(start_t)
    start = 0
    link = 0

    for i in range(n // 2 - 1):
        for j in range(i + 1, n // 2):
            start += table[start_t[i]][start_t[j]] + table[start_t[j]][start_t[i]]
            link += table[link_t[i]][link_t[j]] + table[link_t[j]][link_t[i]]
    res = min(res, abs(start - link))

print(res)