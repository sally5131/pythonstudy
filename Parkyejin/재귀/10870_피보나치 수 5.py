n=int(input())
res=[0,1]

for i in range(n-1):
    sum=res[i]+res[i+1]
    res.append(sum)
print(res[n])