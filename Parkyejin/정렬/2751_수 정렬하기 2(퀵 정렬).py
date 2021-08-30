# 퀵정렬 최대 O(nlogn) 시간복잡도
N=int(input())
a=[]
for i in range(N):
    num=int(input())
    a.append(num)
print(a) # 초기 리스트 출력

def quickSort(a,start,end): # 재귀함수 선언(리스트, 시작인덱스, 종료인덱스)
    if start<end: # 시작인덱스보다 종료인덱스가 클 경우
        left=start # left : 시작인덱스
        pivot=a[end] # pivot : 리스트의 종료인덱스 값
        for i in range(start,end): # 시작인덱스부터 종료인덱스까지 반복
            if a[i]<pivot: # 리스트 인덱스 값이 pivot보다 작은 경우
                a[i],a[left]=a[left],a[i] # 해당 인덱스 값과 left 인덱스 값 swap
                left+=1 # 인덱스 하나 증가
        a[left],a[end]=a[end],a[left] # left 인덱스값과 종료인덱스 값 swap
        quickSort(a,start,left-1)
        quickSort(a,left+1,end)
quickSort(a,0,len(a)-1)
print(a)