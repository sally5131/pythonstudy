# 삽입정렬 최대 O(n^2) 시간복잡도
N=int(input())
a=[]
for i in range(N):
    num=int(input())
    a.append(num)
print(a) # 초기 리스트 출력

for j in range(1,len(a)): # 인덱스 1부터 시작
    for k in range(j,0,-1): # 인덱스의 값이 줄어들면서 삽입할 위치를 찾을 때까지 반복
        if a[k]<a[k-1]: # 앞의 원소가 현재의 원소보다 값이 작다면
            a[k],a[k-1]=a[k-1],a[k] # 값을 swap
        else: break
print(a) # 삽입정렬 후 리스트 출력