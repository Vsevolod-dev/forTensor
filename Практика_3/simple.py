while True:
    choise = input("""
1: Вычисление простого числа
2: Нахождение НОД
3: Нахождение НОК
Выберите цифру?
""")

    if choise == '1':
        #просто число #################################
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
    
    if choise == '2':
        #нод ##########################################
        first = int(input("Введите первое число = "))
        second = int(input("Введите второе число = "))

        while first != 0 and second != 0:
            if first > second:
                first %= second
            else:
                second %= first

        gcd = first + second
        print(f"Наибольший общий делитель = {gcd}")
        ###############################################

    elif choise == '3':
        #нок #########################################       
        first = int(input('Введите первое число = '))
        second = int(input('Введите второе число = '))

        m = first * second
        while first != 0 and second != 0:
            if first > second:
                first %= second          
            else:
                second %= first
        print('Наименьшее общее кратное = ', m // (first + second))
        ###############################################
    
    elif choise == "выход":
        print('Спасибо что воспользовались мной)')
        break;