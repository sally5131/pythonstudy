N=int(input())
res=[]
t=N

for i in range(N):
    if (N==1):
        print()
    else:
        for j in range(2,t+1):
            if(t%j==0):
                res.append(j)
                t=t//j
                break
for k in res:
    print(k)