N=int(input())
# N : N킬로그램 배달
sum=0
# sum : 배달하는 봉지의 최소 개수

for i in range((N//5),-1,-1):
    num=N-(5*i)
    if((i==0) and (num%3!=0)):
        print(-1)
    if (num % 3 == 0):
        j = num // 3
        sum = i + j
        print(sum)
        break