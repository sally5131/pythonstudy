num=input()
# num : N개의 데이터 입력
data=input()
# data : 숫자 리스트 입력
count=0

for i in range(len(data)):
    count+=int(data[i])
print(count)