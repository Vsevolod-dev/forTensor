import time

def banchmark_decorator(func_to_decorate):
    def my_func(x, y):
        ts = time.time()
        func_to_decorate(x, y)
        print(time.time() - ts)
    return my_func

def log_decorator(func_to_decorate):
    def my_func(x, y):
        print('Начало функции...')
        func_to_decorate(x, y)
        print('Конец функции...')
    return my_func

@banchmark_decorator
@log_decorator
def PowX3(x, y):
    time.sleep(1)
    print(x ** y ** x ** y)
    print('Вычисляю...')

PowX3(2, 2)
