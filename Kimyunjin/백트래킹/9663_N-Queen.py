# N = int(input())
#
# def dfs(queen, row, n):
#     cnt = 0
#     if n == row:
#         return 1
#     for col in range(n):
#         queen[row] = col
#         for i in range(row):
#             if queen[i] == queen[row]:  # 세로로 겹치면 안됨
#                 break
#             if abs(queen[i] - queen[row]) == row - i:   # 대각선으로 겹치면 안됨
#                 break
#         else:
#             cnt += dfs(queen, row + 1, n)
#     return cnt
#
#
# def solution(n):
#     queen = [0] * n
#     return dfs(queen, 0, n)
#
# print(solution(N))

N = int(input())
cnt = 0
queen = [0] * N


def check(x):
    for i in range(x):
        if queen[x] == queen[i] or abs(queen[x] - queen[i]) == x - i:
            return False
    return True

def dfs(x):
    global cnt

    if x == N:
        cnt += 1

    else:
        for i in range(N):
            queen[x] = i
            if check(x):
                dfs(x+1)

dfs(0)
print(cnt)