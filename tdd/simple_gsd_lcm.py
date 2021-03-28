def simple(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                print("Число не простое")
                return 'Число не простое'
        else:
            print(num, "Число простое")
            return 'Число простое'
    else: 
        print(num, "Число не простое")
        return 'Число не простое'

def gcd(first, second):
    while first != 0 and second != 0:
            if first > second:
                first %= second
            else:
                second %= first

    return first + second

def lcm(first, second):
    m = first * second
    while first != 0 and second != 0:
        if first > second:
            first %= second          
        else:
            second %= first

    return m // (first + second)

# while True:
#     choise = 0
#     try: 
#         choise = int(input("""
# 1: Вычисление простого числа
# 2: Нахождение НОД
# 3: Нахождение НОК
# 4: Выход
# Выберите цифру?
# """))
#     except ValueError:
#         print('Введите цифру 1 или 2 или 3 или 4')

#     # Просто число
#     if choise == 1:
        
#         while True:
#             try:
#                 num = int(input('Введите число? '))
#             except:
#                 print('Введите ЧИСЛО')
#             else:
#                 break

#         while num < 0:
#             print('Число меньше нуля')
#             num = int(input('Введите число? '))

#         simple(num)
        
#     # НОД
#     if choise == 2:
        
#         while True:
#             try:
#                 first = int(input("Введите первое число = "))
#                 second = int(input("Введите второе число = "))
#             except ValueError:
#                 print("Нужно вводить только ЧИСЛА")
#             else:
#                 break

#         gcd = gcd(first, second)
#         print(f"Наибольший общий делитель = {gcd}")
        
#     # НОК
#     elif choise == 3:
               
#         while True:
#             try:
#                 first = int(input("Введите первое число = "))
#                 second = int(input("Введите второе число = "))
#             except ValueError:
#                 print("Нужно вводить только ЧИСЛА")
#             else:
#                 break

#         lcm = lcm(first, second)

#         print(f'Наименьшее общее кратное = {lcm}')
    
#     elif choise == 4:
#         print('Спасибо что воспользовались мной)')
#         break;