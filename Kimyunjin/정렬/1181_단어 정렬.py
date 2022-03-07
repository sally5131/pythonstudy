import sys

n = int(input())
li = list()
for i in range(n):
    li.append(sys.stdin.readline())
li = list(sorted(set(li)))
li = sorted(li, key=len)
for i in li:
    print(i.rstrip('\n'))