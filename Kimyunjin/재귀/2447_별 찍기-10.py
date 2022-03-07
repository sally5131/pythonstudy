def star_list(n):
    list = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            list.append(n[i%len(n)] + " "*len(n) + n[i%len(n)])
        else:
            list.append(n[i%len(n)]*3)
    return list


star = ["***","* *","***"] # n = 3 일때 정사각형 별
n = int(input())
k = 0
while n != 3:   # k 구하기
    n = int(n / 3)
    k += 1
for i in range(k):
    star = star_list(star)
for j in star:
    print(j)