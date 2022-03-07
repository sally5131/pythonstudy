N=int(input())
res=0
for i in range(1,N+1): # i : 생성자
    A=list(map(int,str(i))) # A : 각 자릿수의 합
    res=i+sum(A) # res: 생성자 + 각 자릿수의 합
    if res==N:
        print(i) # 생성자 출력
        break
    if i==N:
        print(0)