count=int(input())
# count : 단어의 개수
alpha=[]
# alpha : count 만큼의 문자열 리스트
result=0

# count 만큼 문자열 입력
for i in range(count):
    str=input()
    alpha.append(str)

for i in range(len(alpha)):
    answer=[]
    # 문자열에서 연속적인 중복 단어 제거
    for j in range(len(alpha[i])):
        if j==0:
            answer.append(alpha[i][j])
        elif alpha[i][j]!=alpha[i][j-1]:
            answer.append(alpha[i][j])
            # answer : 중복 제거 완료 문자열 리스트
    # answer의 길이와 집합 alpha의 길이가 같다면 result 1 증가
    # set() : 중복제거, 순서상관없음
    if (len(answer) == len(set(alpha[i]))):
        result+=1

print(result)