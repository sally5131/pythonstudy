import sys
N, M=map(int, sys.stdin.readline().split())
a=list(map(int, sys.stdin.readline().split()))

min=sum(a)
def dfs(s, m, cnt):
    global min
    if cnt == M:
        min = min(min, m)
        return
    k=0
    for i in range(s, N):
        if k>=m:
            dfs(i, m+a[i], cnt+1)
            break
        k+=a[i]