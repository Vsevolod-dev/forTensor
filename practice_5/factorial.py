from functools import reduce

# Функция вычисления факториала
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

# Без рекурсии но с модулем.
print(reduce(lambda x, y: x*y, range(1, num + 1))) 

# Рекурсия
fact = lambda n: 1 if n == 0 else n*fact(n - 1) 

print(fact(num)) 