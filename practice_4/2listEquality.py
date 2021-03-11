def fillList(listNum):
    choise = input(""""
Что хотите ввести?
1: Слово
2: Несколько чисел    
""")
    if choise == '1':
        listNum = list(input("Введите слово = "))

    if choise == '2':    
        while True:
            try:
                num = int(input("Введите число = "))
                if not num:
                    break
                else:
                    listNum.append(num)
            except ValueError:
                break

    return listNum

list1 = []
list2 = []
list1 = fillList(list1)
list2 = fillList(list2)

list1.sort()
list2.sort()

print(list1)
print(list2)

print('Совпадают' if list1 == list2 else 'Не Совпадают')
