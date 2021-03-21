from math import sqrt

def quadr_equ(disc, a, b):
    if disc == 0:
        x = -b / (2 * a)
        print("Корень уравнения = ", x)
    elif disc > 0:
        x1 = (-b + pow(disc, 0.5)) / (2*a) #без использования библеотек 
        x2 = (-b - sqrt(disc)) / (2*a) #с использованием библеотекb math
        print(f"""
    Первый корень = {x1}
    Второй корень = {x2}
    """)
    else: 
        realPart = -b / (2*a) #действительная часть
        imagPart = sqrt(-disc)  #мнимая часть 
        x1 = complex(realPart, imagPart)
        x2 = x1.conjugate
        print(f"""
    Первый корень = {x1}
    Второй корень = {x2}
    """)