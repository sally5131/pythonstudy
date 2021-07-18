data=input()
# data : 알파벳 대소문자로 된 단어 입력
data_upper=data.upper()
# data_upper : 대문자로 변환
alpha={}
# alpha : dictionary

# 알파벳 횟수를 alpha에 저장하기
for i in data_upper:
    if i in alpha:
        alpha[i]+=1
    # 문자열이 alpha에 있다면 1증가
    else:
        alpha[i]=1
    # 문자열이 alpha에 없다면 1추가

max=0
index=0

# 최댓값 구하기
for i in alpha:
    if (alpha[i]>max):
        max=alpha[i]
        index=i
    elif (alpha[i]==max):
        index='?'
    # 최댓값 중복이면 ? 출력
print(index)