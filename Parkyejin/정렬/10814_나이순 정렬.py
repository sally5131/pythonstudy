N=int(input())
# N : 온라인 저지 회원의 수
a=[]

for i in range(N):
    age,name=input().split()
    a.append([int(age),name,i])

a.sort(key=lambda person: (person[0]))
# 각 행의 첫번재 인덱스 기준, 나이 기준으로 정렬

for person in a:
    print(person[0],person[1])