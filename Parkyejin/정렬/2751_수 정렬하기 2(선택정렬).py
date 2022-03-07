# 선택정렬 최대 O(n^2) 시간복잡도
N=int(input())
a=[]
for i in range(N):
    num=int(input())
    a.append(num)
print(a) # 초기 리스트 출력

for j in range(len(a)-1): # 리스트의 길이 -1만큼 반복
    for k in range(j+1,len(a)): # 인덱스 j+1부터 리스트 길이만큼 반복
        if a[j]>a[k]: # 인덱스 j의 값이 인덱스 k의 값보다 작으면
            a[j],a[k]=a[k],a[j] # 값 swap
print(a) # 선택정렬 후 리스트 출력
