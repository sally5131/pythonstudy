import math
M=int(input())
N=int(input())
res=[]

for i in range(M,N+1):
    if(i!=1):
        check=True
        for j in range(2,i):
            if i%j==0:
                check=False
                break
        if check==True:
            res.append(i)

if(len(res)==0):
    print(-1)
else:
    print(sum(res))
    print(res[0])