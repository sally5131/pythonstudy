N=int(input())
# N : 수의 개수
nums=map(int,input().split())
# 여러개의 정수를 공백을 기준으로 입력받기
res=0

for i in nums:
    count=0
    if i>1:
        for j in range(2,i):
            if (i%j==0):
                count=count+1
        if (count==0):
            res=res+1
print(res)