import math
M,N=map(int,input().split())
# M, N : M이상 N이하

numbers={x for x in range(M,N+1) if x==2 or x%2==1}
# numbers : 2와 홀수 집합

for num in range(3,int(math.sqrt(N))+1,2):
    # 3~N의 제곱근 중에서 홀수
    numbers-={i for i in range(num*2,N+1,num)}
    # num의 홀수배는 numbers 집합에서 제외

for j in sorted(numbers):
    # numbers 증가순으로 정렬
    if(j>1):
        print(j)