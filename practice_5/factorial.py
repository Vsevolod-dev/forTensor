from functools import reduce

def factorial(num):
    fac = 1
    while num:
        fac *= num
        num -= 1
    return fac



try:
    num = int(input('Введите число: '))
except ValueError:
    print('ЧИСЛООООО')

print(factorial(num))

print(reduce(lambda x, y: x * y, range(1, num + 1))) #без рекурсии но с модулем

fact = lambda n: 1 if n == 0 else n * fact(n - 1) #рекурсия
print(fact(num)) 