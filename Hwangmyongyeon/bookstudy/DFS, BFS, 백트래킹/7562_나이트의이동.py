import sys
import math
from collections import deque
T = int(sys.stdin.readline())

dx = (-2, -2, -1, -1, +1, +1, +2, +2)
dy = (-2, +2, -1, +1, -2, +2, -1, +2)

for _ in range(T):
    I = int(sys.stdin.readline())

    board = list([False] * I for _ in range(I))
    chk = list([False] * I for _ in range(I))

    sr, sc = map(int, sys.stdin.readline().split())
    dr, dc = map(int, sys.stdin.readline().split())

    board[dr][dc] = True

    dq = deque()
    dq.append((sr, sc, 0))
    chk[sr][sc] = True

    while dq:
        r, c, cnt = dq.popleft()
        if board[r][c]:
            print(cnt)
            break
        for i in range(8):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < I and 0 <= nc < I and not chk[nr][nc]:
                dq.append((nr, nc, cnt+1))
                chk[nr][nc] = True


