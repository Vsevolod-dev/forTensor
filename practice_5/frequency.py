from modules import freq_module

# Разделение по пробелам для предложения и нахождения количества слов. 
def freq_sentence(sentence):
    return len(sentence.split(' '))

# Разделение по пробелам и точке для целого текста 
# и нахождения количества предложений.
def freq_text(text): 
    return len(text.split('. '))

# Выбор действия
choise = input("""
Что хотите ввести?
1: подсчета частоты вхождений символов в текст
2: подсчета количества слов в тексте
3: посчета количества предложений в тексте    
""")
if choise == '1':
    word = input('Введите слово: ')
    print(freq_module(word))

if choise == '2':    
    sentence = input('Введите предложение: ')
    print(f'Слов в предложении: {freq_sentence(sentence)}')

if choise == '3':
    text = input('Введите текст: ')
    print(f'Предложений в тексте: {freq_text(text)}')

# Программа подсчета частоты вхождений символов в текст с использованием lambda.
freq_word = {}

word = input('Введите слово: ')

for i in word: freq_word[i] = (lambda i: freq_word.get(i, 0) + 1)(i)

print(freq_word)