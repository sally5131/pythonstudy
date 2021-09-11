import sys

n = int(input())
li = list()
for i in range(n):
    li.append(int(sys.stdin.readline()))
for i in sorted(li):
    print(i)