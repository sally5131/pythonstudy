def factorial(num):
    res = 1
    if num > 0 :
        res = num * factorial(num - 1)
    return res


n = int(input())
print(factorial(n))