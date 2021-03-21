while True:

    color = input('Введите цвет ')

    if color == 'красный':
        print('Стой')
    elif color == 'желтый':
        print('Подожди немного')
    elif color == 'зеленый':
        print('Иди')
    elif color == 'выход':
        print('Спасибо что воспользовались мной)')
        break;
    else: 
        print('Такого цвета нет')
