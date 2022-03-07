N=int(input())
# N : 단어의 개수
a=[]

for i in range(N):
    a.append(input())
set_alpha=list(set(a)) # set_alpha : 리스트 a에서 중복 제거

sort_alpha=[]
for j in set_alpha:
    sort_alpha.append((len(j),j)) # sort_alpha : 알파벳의 길이와 알파벳을 저장

res=sorted(sort_alpha) # res : sort_alpha를 사전 순으로 정렬

for k, t in res:
    print(t)