while True:
    choise = 0
    try: 
        choise = int(input("""
1: Вычисление простого числа
2: Нахождение НОД
3: Нахождение НОК
4: Выход
Выберите цифру?
"""))
    except ValueError:
        print('Введите цифру 1 или 2 или 3 или 4')

    if choise == 1:
        #просто число #################################
        while True:
            try:
                num = int(input('Введите число? '))
            except:
                print('Введите ЧИСЛО')
            else:
                break

        while num < 0:
            print('Число меньше нуля')
            num = int(input('Введите число? '))
                
        if num > 1:
            for i in range(2, num//2):
                if (num % i) == 0:
                    print("Число не простое")
                    break
            else:
                print(num, "Число простое")
        else: 
            print(num, "Число не простое")
        ###############################################
    
    if choise == 2:
        #нод ##########################################
        while True:
            try:
                first = int(input("Введите первое число = "))
                second = int(input("Введите второе число = "))
            except ValueError:
                print("Нужно вводить только ЧИСЛА")
            else:
                break

        while first != 0 and second != 0:
            if first > second:
                first %= second
            else:
                second %= first

        gcd = first + second
        print(f"Наибольший общий делитель = {gcd}")
        ###############################################

    elif choise == 3:
        #нок #########################################       
        while True:
            try:
                first = int(input("Введите первое число = "))
                second = int(input("Введите второе число = "))
            except ValueError:
                print("Нужно вводить только ЧИСЛА")
            else:
                break

        m = first * second
        while first != 0 and second != 0:
            if first > second:
                first %= second          
            else:
                second %= first

        lcm = m // (first + second)

        print(f'Наименьшее общее кратное = {lcm}')
        ###############################################
    
    elif choise == 4:
        print('Спасибо что воспользовались мной)')
        break;