import math
n = int(input())
li = list()

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # 둘 사이의 거리

    if dis == 0 and r1 == r2:   # 두 원이 겹칠 때
        li.append(-1)
    elif abs(r1 - r2) == dis or r1 + r2 == dis:  # 내접, 외접일 때
        li.append(1)
    elif abs(r1 - r2) < dis < (r1 + r2):  # 두 원이 두 점에서 만날 때
        li.append(2)
    else:
        li.append(0)

for i in range(n):
    print(li[i])