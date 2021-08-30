N=int(input())
num=list(map(int,input().split()))

sort_num=sorted(list(set(num))) # 중복값 제거, 오름차순 정렬
dict={sort_num[i]:i for i in range(len(sort_num))}
# dict : sort_num 리스트 값에 인덱스를 지정
for i in num:
    print(dict[i],end=' ')