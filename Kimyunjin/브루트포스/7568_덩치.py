n = int(input())
li = []
res = []

for i in range(n):
    w, h = map(int, input().split())
    li.append([w, h])

for j in li:
    cnt = 0
    for k in li:
        if j[0] < k[0] and j[1] < k[1]:
            cnt += 1
    res.append(cnt + 1)

for i in range(len(res)):
    print(res[i], end=' ')