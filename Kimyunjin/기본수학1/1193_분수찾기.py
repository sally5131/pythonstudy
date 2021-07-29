x = int(input()) # x번째 분수
line = 1

while x > line:
    x -= line
    line += 1

if line % 2 ==0:    # 짝수일때
    a = x   # 분자
    b = line - x + 1    # 분모
else:   # 홀수일때
    a = line - x + 1    # 분자
    b = x   # 분모

print(a, "/", b, sep='')