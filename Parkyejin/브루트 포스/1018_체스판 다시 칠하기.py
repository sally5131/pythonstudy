N,M=map(int,input().split())
# NXM 크기의 정사각형
board=[]

for i in range(N):
    board.append(input())

res=[]
for i in range(N-7): # NXM 크기에서 8X8 크기의 정사각형
    for j in range(M-7):
        count=0 # 다시 칠해야하는 정사각형의 개수
        index=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                # 체스판의 첫번째 인덱스가 W로 시작
                if index%2==0:
                    if board[k][l]!="W":
                        count+=1
                else:
                    if board[k][l]!="B":
                        count+=1
                if l!=j+7:
                    # 마지막 인덱스가 아닌 경우
                    index+=1

        res.append(min(count,64-count))
        # 체스판의 첫번째 인덱스가 B로 시작하는 경우와 count 비교
print(min(res))