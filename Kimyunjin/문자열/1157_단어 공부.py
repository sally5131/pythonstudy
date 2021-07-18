word = input().upper()
word_list = list(set(word)) # 중복 제거
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[cnt.index(max(cnt))])