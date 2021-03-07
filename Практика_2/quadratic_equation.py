from math import sqrt
from sys import exit

a = float(input('Введите первый коэфицент? '))
b = float(input('Введите второй коэфицент? '))
c = float(input('Введите третий коэфицент? '))

if a == 0:
    x = -c / b
    print("Обычное линейное уравнение, где корень = ", x)
    exit()

disc = b**2 - 4 * a * c

if disc == 0:
    x = -b / (2 * a)
    print("Корень уравнения = ", x)
elif disc > 0:
    x1 = (-b + pow(disc, 0.5)) / (2 * a) #без использования библеотек 
    x2 = (-b - sqrt(disc)) / (2 * a) #с использованием библеотекb math
    print("Первый корень = ", x1, "\nВторой корень = ", x2)
else: #допустим решаем с комплексными числами
    deistvChast = -b / (2 * a) #действительная часть
    mnimChast = sqrt(-disc)  #мнимая часть 
    x1 = complex(deistvChast, mnimChast)
    x2 = complex(deistvChast, -mnimChast)
    print("Первый корень = ", x1)
    print("Второй корень = ", x2)