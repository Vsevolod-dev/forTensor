from sys import exit

def calc(a=1, b=2, operation="+"):
    def add(a1, b1):
        return a1 + b1

    def remove(a1, b1):
        return a1 - b1

    def multiply(a1, b1):
        return a1 * b1

    def divide(a1, b1):
        return a1 / b1

    def intPart(a1, b1):
        return a1 // b1

    def mod(a1, b1):
        return a1 % b1

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
