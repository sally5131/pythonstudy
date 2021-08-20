N=int(input())
# N : 전체 사람의 수
person=[]

for i in range(N):
    x,y=map(int,input().split())
    # x : 몸무게, y : 키
    person.append((x,y))

for j in person:
    rank=1
    for k in person:
        if(j[0]<k[0] and j[1]<k[1]):
            rank+=1
    print(rank, end=" ")