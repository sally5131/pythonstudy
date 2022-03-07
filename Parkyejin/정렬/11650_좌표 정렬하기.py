N=int(input())
# N: 점의 개수
a=[]

for i in range(N):
    x,y=map(int,input().split())
    a.append((x,y))

a.sort()
for j in range(N):
    print(a[j][0], a[j][1])