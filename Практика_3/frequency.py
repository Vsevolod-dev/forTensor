def freq(str):
    freq_obj = {}

    for i in str:
        if i in freq_obj:
            freq_obj[i] += 1
        else:
            freq_obj[i] = 1

    return freq_obj

while True:
    choise = input("""
1: Частота использования цифр в диапазоне чисел
2: Частота использования символов в тексте
Выберите цифру?
""")

    if choise == '1':
        begin = int(input("Введите начало массива = "))
        end = int(input("Введите начало массива = "))

        strNum = ''
        while begin <= end:
            strNum += str(begin)
            begin += 1

        print(freq(strNum))

    if choise == '2':
        word = input("Введите слово = ")
        print(freq(word))

    if choise == 'выход':
        print('Спасибо что воспользовались мной)')
        break;