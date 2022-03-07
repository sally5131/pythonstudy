t = int(input())
li = list()

for i in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        num = h * 100 + (n // h)
    else:
        num = (n % h) * 100 + (n // h) + 1
    li.append(num)

for j in range(len(li)):
    print(li[j])