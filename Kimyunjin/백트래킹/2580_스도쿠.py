import sys

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
empty = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j]==0]

def candidate(x, y):    # 빈 칸에 들어갈 수 있는 숫자 후보
    nums = [i+1 for i in range(9)]
    # 행열 검사
    for k in range(9):
        if sudoku[x][k] in nums:
            nums.remove(sudoku[x][k])
        if sudoku[k][y] in nums:
            nums.remove(sudoku[k][y])
    # 3x3 검사
    x = x//3
    y = y//3
    for i in range(x*3, (x+1)*3):
        for j in range(y*3, (y+1)*3):
            if sudoku[i][j] in nums:
                nums.remove(sudoku[i][j])
    # 후보 리턴
    return nums

def dfs(cnt):
    if cnt == len(empty):
        for row in sudoku:
            print(*row)
        return
    (i, j) = empty[cnt]
    candi = candidate(i, j)
    for num in candi:
        sudoku[i][j] = num
        dfs(cnt+1)
        sudoku[i][j] = 0

dfs(0)