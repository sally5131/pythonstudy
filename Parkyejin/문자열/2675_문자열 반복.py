T=int(input())
# T : 테스트 케이스 반복 횟수 입력, 정수형

# 입력받은 테스트 케이스 횟수만큼 반복
for i in range(T):
    R, S=input().split()
    # 공백을 기준으로 입력값 분리
    # R : 문자 반복 횟수 입력, 정수형
    # S : 반복할 문자열 입력, 문자형
    result=''
    # result : 결과값 저장
    for j in S:
        result+=int(R)*j
    # S의 j번째 문자를 R만큼 중복해서 result 에 저장
    print(result)