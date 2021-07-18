S=input()
# S : 입력 리스트
alpha=list('abcdefghijklmnopqrstuvwxyz')
# alpha : 알파벳 소문자 리스트
array=[-1]*len(alpha)
# array : alpha의 길이만큼 -1로 이루어진 리스트

for i in range(len(S)):
    if array[alpha.index(S[i])]==-1:
        array[alpha.index(S[i])]=i
# alpha 리스트의 인덱스와 array의 인덱스가 같으면 i

for j in range(len(array)):
    print(array[j], end=' ')
# array 출력






