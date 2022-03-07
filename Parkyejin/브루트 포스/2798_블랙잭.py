N,M=map(int,input().split())
# N : 카드의 개수, M : M과 최대한 가깝게
num=list(map(int,input().split()))
sum=0

for i in range(0,len(num)-2):
    for j in range(i+1,len(num)-1):
        for k in range(j+1,len(num)):
            if(num[i]+num[j]+num[k]>M):
                continue
            else:
                sum=max(sum,num[i]+num[j]+num[k])
print(sum)