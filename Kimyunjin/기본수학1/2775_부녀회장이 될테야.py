t = int(input())

for i in range(t):
    k = int(input())    # k층
    n = int(input())    # n호
    num = [x for x in range(1, n+1)]

    for j in range(k):
        for m in range(1, n):
            num[m] += num[m-1]
    print(num[-1])