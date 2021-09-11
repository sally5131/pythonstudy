import sys

n = int(input())
li = list(map(int, sys.stdin.readline().split()))
sortli = list(sorted(set(li)))
dic = {sortli[i]:i for i in range(len(sortli))}
for i in li:
    print(dic[i], end=' ')