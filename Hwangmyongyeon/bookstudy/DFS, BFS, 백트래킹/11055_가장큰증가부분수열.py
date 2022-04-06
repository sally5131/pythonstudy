import sys
N=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
b=[]
maxV=0
def dfs(i, num, sum): # i번째 볼 차례, 고른 마지막 수열 수 = num, 수열 합 sum
    if i == N or a[i]<=num:
        global maxV
        maxV=max(maxV, sum)
        return
    for i in range(i, N):
        if a[i]>num:
            b.append(a[i])
            dfs(i+1, a[i], sum+a[i])
            b.pop()
    return
dfs(0, 0, 0)
print(maxV)