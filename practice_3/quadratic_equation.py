from math import sqrt
from sys import exit
from modules import quadratic_equation_module as qem

# Проверка первого коэфицента
while True:
    try:
        a = float(input('Введите первый коэфицент? '))
    except ValueError:
        print('Введите число')
    else:
        break

# Проверка второго коэфицента
while True:
    try:
        b = float(input('Введите второй коэфицент? '))
    except ValueError:
        print('Введите число')
    else:
        break

# Проверка третьего коэфицента
while True: 
    try:
        c = float(input('Введите третий коэфицент? '))
    except ValueError:
        print('Введите число')
    else:
        break


# Линейное уравнение
if a == 0:
    if b == 0:
        print('Неправильно заданы параметры, запустите программу заново')
        exit()
    else:
        x = -c / b
        print(f"Обычное линейное уравнение, где корень = {x}") 

if b == 0 and c == 0:
    x = 0
    print(f"Корень уравнения = {x}")
    exit()

disc = b**2 - 4*a*c

if b == 0:
    if -c / a:
        realPart = -b / (2*a) #действительная часть
        imagPart = sqrt(-disc)  #мнимая часть 
        x1 = complex(realPart, imagPart)
        x2 = complex(realPart, -imagPart)
    else:
        x1 = sqrt(-c / a)
        x2 = -x1
    print(f"""
Первый корень = {x1}
Второй корень = {x2}
""")
    exit()

if c == 0:
    x1 = 0
    x2 = -b / a
    print(f"""
Первый корень = {x1}
Второй корень = {x2}
""")
    exit()


qem(disc, a, b)