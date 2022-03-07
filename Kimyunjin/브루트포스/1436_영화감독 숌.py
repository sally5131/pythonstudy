n = int(input())
num = 0
cnt = 0

while True:
    num += 1
    if str(num).find("666") != -1:
        cnt += 1
        if cnt == n:
            break
print(num)