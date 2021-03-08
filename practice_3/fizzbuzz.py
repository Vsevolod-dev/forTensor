for i in range(0, 101):
    # if i % 5 == 0 and i % 3 == 0:
    #     print('FizzBuzz')
    # elif i % 5 == 0:
    #     print('Buzz')
    # elif i % 3 == 0:
    #     print('Fizz')
    # else:
    #     print(i)
    # а теперь запись в одну строчку с наименьшей длиной кода)
    print('FizzBuzz') if i % 5 == 0 and i % 3 == 0 else print('Buzz') if i % 5 == 0 else print('Fizz') if i % 3 == 0 else print(i)