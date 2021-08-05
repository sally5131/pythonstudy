n = int(input())
li = list(map(int, input().split(" ")))
total = 0

for i in range(n):
    flag = True
    if li[i] < 2:
        continue
    for j in range(2, li[i]):
        if li[i] % j == 0:
            flag = False
            break
    if flag:
        total += 1
print(total)