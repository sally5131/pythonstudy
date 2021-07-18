A, B=input().split()
# A, B : 공백 구분하여 입력받기, 정수형
rev_A=A[::-1]
# rev_A : A의 값을 거꾸로 초기화
rev_B=B[::-1]
# rev_B : B의 값을 거꾸로 초기화

# A와 B 사이의 최댓값 구하기
if(rev_A>=rev_B):
    print(rev_A)
else:
    print(rev_B)

