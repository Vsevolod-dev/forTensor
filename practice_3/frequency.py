def freq(str):
    freq_obj = {}

    for i in str:
        if i in freq_obj:
            freq_obj[i] += 1
        else:
            freq_obj[i] = 1

    return freq_obj

def fill(begin, end):
    strNum = ''

    # Если первый элемент больше последнего
    # строка заполняется элементами от начала до конца
    # (заполнение с элементами с конца)
    if end < begin:
        while end < begin:
            strNum += str(begin)
            begin -= 1

    # Если первый элемент меньше последнего 
    # строка заполняется элементами от начала до конца
    # (заполнение с элементами с начала)      
    if begin <= end:
        while begin <= end:
            strNum += str(begin)
            begin += 1
    
    return strNum

while True:
    choise = 0
    try:
        choise = int(input("""
1: Частота использования цифр в диапазоне чисел
2: Частота использования символов в тексте
3: Выход
Выберите цифру?
"""))
    except ValueError:
        print('Введите цифру 1 или 2 или 3')

    if choise == 1:
        begin = 0
        end = 0
        while True:
            try:
                begin = int(input("Введите начало массива = "))
                end = int(input("Введите конец массива = "))
            except ValueError:
                print("Нужно вводить только числа")
            else:
                break
        
        # Заполнение строки
        strNum = fill(begin, end)
      
        print(strNum)
        print(freq(strNum))

    if choise == 2:
        word = str(input("Введите слово = "))
        print(freq(word))

    if choise == 3:
        print('Спасибо что воспользовались мной)')
        break;