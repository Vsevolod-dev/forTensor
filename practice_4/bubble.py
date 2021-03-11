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
    

def buble(listNum):
    for i in range(len(listNum) - 1):
        for j in range(len(listNum)-i-1):
            if listNum[j] > listNum[j+1]:
                listNum[j], listNum[j+1] = listNum[j+1], listNum[j]
    return listNum


listNum = []
print(buble(fillList(listNum)))

