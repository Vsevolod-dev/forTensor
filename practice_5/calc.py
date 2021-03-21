from sys import exit

def calc(a=1, b=2, operation="+"):
    """Калькулятор базовых операций
    
    Keyword arguments:
    a -- первый аргумент
    b -- второй аргумент
    operation -- знак оперции
    """

    # Функция сложения
    def add(a1, b1):
        return a1 + b1
    
    # Функция вычитания
    def remove(a1, b1):
        return a1 - b1
    
    # Функция умножения
    def multiply(a1, b1):
        return a1 * b1
    
    # Функция деления
    def divide(a1, b1):
        return a1 / b1

    # Функция нахождения целой части.
    def intPart(a1, b1):
        return a1 // b1

    # Функция нахождения остатка.
    def mod(a1, b1):
        return a1 % b1

    # Функция возведения в степень.
    def pow(a1, b1):
        return a1 ** b1

    selector = {
        "+": add,
        "-": remove,
        "*": multiply,
        "/": divide,
        "//": intPart,
        "%": mod,
        "**": pow
        }

    return selector[operation](a, b)

while True:
    expression = input("Введите выражение в формате: 'число оператор число'\n")
    if expression:
        try: 
            exSp = expression.split(" ")
            print(calc(float(exSp[0]), float(exSp[2]), exSp[1]))
        except ValueError:
            print("ОШИБКА: Не число")
        except TypeError:
            print("ОШИБКА: Строки нельзя делить на число")
        except ZeroDivisionError:
            print("ОШИБКА: Деление на ноль")
        except KeyError:
            print("ОШИБКА: вы ввели несуществующую операцию")
        except OverflowError:
            print("ОШИБКА: результат выражения слишком большой")
        except Exception:
            print("ОШИБКА: Что-то пошло не так")
        else:
            print("ОШИБКА: Задача успешно завершена")
        finally:
            print("ОШИБКА: Задача завершена")
    else:
        exit()
