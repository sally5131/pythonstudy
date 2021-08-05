def get_prime_list(num):
    prime_list = list()
    for i in range(2, num):
        flag = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            prime_list.append(i)
    return prime_list


t = int(input())
prime_list = get_prime_list(10001)
for i in range(t):
    num = int(input())
    k = num // 2
    for j in range(k, 1, -1):  # k부터 2까지 1씩 감소
        if (num - j in prime_list) and (j in prime_list):
            print(j, num - j)
            break