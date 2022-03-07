N=int(input())
a=[]
for i in range(N):
    num=int(input())
    a.append(num)

a.sort() # 오름차순 정렬
for j in a:
    print(j) # 파이썬 내장 정렬 메소드

# 내림차순 정렬 : a.sort(reverse=True)