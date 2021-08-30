# 버블정렬 최대 O(n^2) 시간복잡도
N=int(input())
a=[]
for i in range(N):
    num=int(input())
    a.append(num)
print(a) # 초기 리스트 출력

for j in range(1,len(a)): # 인덱스 1부터 반복
    for k in range(0,len(a)-1): # 인덱스 0부터 len(a)-2까지 반복
        if a[k]>a[k+1]: # 현재 인덱스의 값이 다음 인덱스의 값보다 크면
            a[k],a[k+1]=a[k+1],a[k] # 값 swap
print(a) # 버블 정렬 후 리스트