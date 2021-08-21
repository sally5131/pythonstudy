n = int(input())
li = list()
for i in range(1, n+1):
    sum = i
    for j in str(i):
        sum += int(j)
    if sum == n:
        print(i)
        break
    elif i == n:
        print(0)