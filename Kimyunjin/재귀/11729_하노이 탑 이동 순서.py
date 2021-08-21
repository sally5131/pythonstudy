def hanoi(n, a, b, c):
    if n == 1:
        move.append([a, c])
    else:
        hanoi(n-1, a, c, b)
        move.append([a, c])
        hanoi(n-1, b, a, c)


n = int(input())    # 원판의 개수
move = list()   # 이동 리스트
hanoi(n, 1, 2, 3)
print(len(move))
for i in range(len(move)):
    for j in range(2):
        print(move[i][j], end=' ')
    print()