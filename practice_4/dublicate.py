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

# Функция поиска значений, которые уже встречались.
def delDub(list):
    newList = []
    # Реверс, для условия о том, что стоит условие про предыдущие элементы. 
    list.reverse() 
    for i in list:
        if i not in newList:
            newList.append(i)
    newList.reverse()
    return newList



list1 = []
list1 = fillList(list1)
print(list1)
list1 = delDub(list1)
print(list1)
