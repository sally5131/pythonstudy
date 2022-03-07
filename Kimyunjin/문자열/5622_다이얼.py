word = input()
sum = 0
for i in word:
    if 'A' <= i <= 'C':
        sum += 3
    elif 'D' <= i <= 'F':
        sum += 4
    elif 'G' <= i <= 'I':
        sum += 5
    elif 'J' <= i <= 'L':
        sum += 6
    elif 'M' <= i <= 'O':
        sum += 7
    elif 'P' <= i <= 'S':
        sum += 8
    elif 'T' <= i <= 'V':
        sum += 9
    elif 'W' <= i <= 'Z':
        sum += 10

print(sum)