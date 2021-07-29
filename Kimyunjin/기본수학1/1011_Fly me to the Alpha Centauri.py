t = int(input())
li = list()

for i in range(t):
    x, y = map(int, input().split())    # x : 현재위치, y : 목표위치
    dis = y - x    # 이동 거리
    cnt = 0  # 이동 횟수
    move = 1  # 이동하는 거리
    sum = 0  # 이동한 거리의 합
    while sum < dis:
        cnt += 1
        sum += move
        if cnt % 2 == 0:  # 이동 횟수가 2의 배수일 때
            move += 1
    li.append(cnt)
for i in range(len(li)):
    print(li[i])