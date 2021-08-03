import math
T=int(input())
# T : 테스트 케이스의 개수

numbers={x for x in range(2,10001) if x==2 or x%2==1}
# numbers : 2와 홀수 집합
for num in range(3, int(math.sqrt(10000)+1),2):
    # 3~10000의 제곱근 중 홀수
    numbers-={i for i in range(num*2,10000,num)}
    # num의 홀수배는 numbers 집합에서 제외

for i in range(T):
    n=int(input())
    k=n//2
    # k : n을 2로 나눈 몫
    for j in range(k,1,-1):
        # k로부터 차이가 적은 두 소수 구하기
        if (n-j in numbers and j in numbers):
            # 두 수 모두 numbers에 포함
            print(j, n-j) # 작은 수부터 출력
            break