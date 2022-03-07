N=int(input())
# N번째 영화
count=0
num=666

while True:
    if "666" in str(num): # num에 666이 있으면 count 1추가
        count+=1
    if count==N: # count가 N번째와 같으면 반복문 종료
        print(num)
        break
    num+=1  # num에 666이 없으면 num에 1를 더함