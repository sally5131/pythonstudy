import sys
input= sys.stdin.readline

s= input()
arr= s.split() #공백문자로 문자열을 쪼개 리스트로 반환됨.
arr= [i for i in arr if i != " "]
print(len(arr))