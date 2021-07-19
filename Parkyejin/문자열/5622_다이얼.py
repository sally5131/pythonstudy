import sys
input=sys.stdin.readline

dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
alpha=input()
# alpha : 대문자 입력
time=0

for i in alpha:
 for j in dial:
  if i in j:
   time+=dial.index(j)+3

print(time)
# 다이얼을 걸기 위해서 필요한 최소 시간 출력