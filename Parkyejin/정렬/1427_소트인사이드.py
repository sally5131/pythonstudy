N=int(input())
a=list(map(int,str(N))) # 각 자리의 숫자를 리스트로 변환
a.sort(reverse=True) # 내림차순 정렬
for i in a:
    print(i,end='')
# sum=0
# b=len(a)-1
# for i in range(len(a)):
#     t=10**(b)
#     if(b>=0):
#         sum+=a[i]*t
#         b-=1
#     else: break
# print(sum)