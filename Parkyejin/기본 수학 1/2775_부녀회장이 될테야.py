T=int(input())
# T : Test case의 수
res=[]
# res : 해당 집의 거주민 수 리스트

for i in range(T):
    k=int(input())
    # k : 층 수
    n=int(input())
    # n : 호 수
    people=[i for i in range(1,n+1)]
    # people : 0층의 n호수 까지의 값을 저장 (1, 2, 3, ... n)
    for t in range(k):
        for j in range(1,n):
            people[j]+=people[j-1]
    res.append(people[n-1])

for i in res:
    print(i)