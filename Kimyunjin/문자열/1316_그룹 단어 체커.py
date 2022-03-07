n = int(input())
sum = 0

for i in range(n):
    m = 1
    word = input()
    word_list = list(set(word))  # 중복 제거

    for j in word_list:
        if j*(word.count(j)) in word:
            continue
        else:
            m = 0
            break

    if m == 1:
        sum += 1
print(sum)

