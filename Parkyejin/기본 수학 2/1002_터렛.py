import math
T=int(input())
# T : 테스트 케이스의 개수
res=[]

for i in range(T):
    max=0
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    dist=math.sqrt((x1-x2)**2+(y1-y2)**2)
    # dist : 두 점 사이의 길이
    if(dist==0 and r1==r2):
        res.append(-1)
        # 두 원의 위치관계 - 무한개의 점에서 만나는 경우
    elif(dist<(r1+r2) and dist>abs(r1-r2)):
        res.append(2)
        # 두 원의 위치관계 - 두 점에서 만나는 경우
    elif(dist==(r1+r2) or dist==abs(r1-r2)):
        res.append(1)
        # 두 원의 위치관계 - 한 점에서 만나는 경우
    elif(dist>(r1+r2) or dist<abs(r1-r2)):
        res.append(0)
        # 두 원의 위치관계 - 만나지 않는 경우

for j in res:
    print(j)