T=int(input())
# T : T개의 테스트 데이터
result=[]
# result : 방 호수 리스트
sum=0
# sum : 방 호수
for i in range(T):
    H, W, N=map(int,input().split())
    # H : 호텔의 층 수
    # W : 각 층의 방 수
    # N: N번째 손님
    Y=(N%H)*100
    # Y : 방의 층 수
    X=(N//H)+1
    # X : 방의 번호
    if N%H==0:
    # 방의 층수가 0인 경우
        Y=H*100
        X=N//H
    sum=Y+X
    result.append(sum)

for i in result:
    print(i)