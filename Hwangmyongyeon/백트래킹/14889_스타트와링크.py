import sys
N=int(sys.stdin.readline())
arr=list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
res=[]
def bt(idx, a, b):
    if idx==N:
        if len(a)!=N//2 or len(b)!=N//2:
            return
        sum_a=0
        sum_b=0
        for i in range(N//2):
            for j in range(N//2):
                if i==j:
                    continue
                sum_a+=arr[a[i]][a[j]]
                sum_b+=arr[b[i]][b[j]]
        res.append(abs(sum_a-sum_b))
        return
    if len(a)>N//2 or len(b)>N//2:
        return
    for i in range(idx, N):
        bt(i+1, a+[i], b)
        bt(i+1, a, b+[i])
bt(0, [], [])
print(min(res))