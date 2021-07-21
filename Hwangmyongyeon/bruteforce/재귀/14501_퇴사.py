import sys
N= int(sys.stdin.readline())
T, P= [], []
for _ in range(N):
    t, p= map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)
a=[]
def go(i, res):
    if i>7:
        a.append(res)
        return
    go(i+T[i], res+P[i])
    go(i+1, res)

go(0, 0)
print(max(a))