N=int(input())
res=1

if(N==0):
    print(res)
else:
    for i in range(N):
        res*=N
        N-=1
    print(res)