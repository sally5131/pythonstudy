n, m = map(int, input().split())
card = list(map(int, input().split()))

from itertools import combinations
c = list(combinations(card, 3))
res = []
for i in range(len(c)):
    if sum(c[i]) <= m:
        res.append(sum(c[i]))
print(max(res))