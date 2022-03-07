import sys

n = int(input())
li = list()
for i in range(n):
    [x, y] = sys.stdin.readline().split()
    li.append([int(x), y])
li.sort(key=lambda x:x[0])
for j in li:
    print(j[0], j[1])