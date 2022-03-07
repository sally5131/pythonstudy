def stars(n):
    matrix=[]
    for i in range(3*len(n)):
        if i//len(n)==1: #3으로 나눈 몫이 1일 경우 빈칸
            matrix.append(n[i%len(n)]+" "*len(n)+n[i%len(n)])
        else: # 몫이 1이 아닌 경우 3*3 크기의 star 형태
            matrix.append(n[i%len(n)]*3)
    return(list(matrix))

n=int(input())
# n : 3의 거듭제곱
k=0
star=["***",'* *','***']

while n!=3:
    n=int(n/3)
    k+=1
for i in range(k):
    star=stars(star)
for i in star:
    print(i)