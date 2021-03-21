from sys import exit
from modules import quadratic_equation_module as qem

a = float(input('Введите первый коэфицент? '))
b = float(input('Введите второй коэфицент? '))
c = float(input('Введите третий коэфицент? '))

if a == 0:
    x = -c / b
    print("Обычное линейное уравнение, где корень = ", x)
    exit()

disc = b**2 - 4*a*c

qem(disc, a, b)