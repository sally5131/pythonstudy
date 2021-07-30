import math
T=int(input())
# T : 테스트케이스의 개수
res=[]
# res : 결과
for i in range(T):
    x, y=map(int,input().split())
    # x : 현재 위치
    # y : 목표 위치
    dist=int(y-x)
    # dist : x지점으로부터 y지점까지의 거리
    if dist<=3:
        res.append(dist)
    else:
        num=int(math.sqrt(dist))
        # math.sqrt() : 제곱근 함수
        if dist==num**2: # d=4,9,16,25,..
            res.append((2*num)-1) # 3,4,5,..
        elif num**2<dist<=num**2+num: # d=5,6/10,11,12/..
            res.append(2*num) # 4,4/6,6,6/..
        else: # d=7,8/..
            res.append((2*num)+1) # 5,5/..

for i in res:
    print(i)