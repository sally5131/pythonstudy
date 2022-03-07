import sys

n = int(sys.stdin.readline())
li = list()

for i in range(n):
    [x, y] = map(int, sys.stdin.readline().split())
    li.append([x, y])
li = sorted(li)
for j in range(n):
    print(li[j][0], li[j][1])