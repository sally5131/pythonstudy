n, m = map(int, input().split())
original = []
count = []

for i in range(n):
    original.append(input())

for a in range(n-7):
    for b in range(m-7):
        startW = 0
        startB = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        startW += 1
                    if original[i][j] != 'B':
                        startB += 1
                else:
                    if original[i][j] != 'B':
                        startW += 1
                    if original[i][j] != 'W':
                        startB += 1
        count.append(min(startW, startB))

print(min(count))