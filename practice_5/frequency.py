
def freq_word(word):
    freq_word = {}
    for i in word: freq_word[i] = freq_word[i] + 1 if i in freq_word else 1
    return freq_word

def freq_sentence(sentence):
    return len(sentence.split(' '))

def freq_text(text): 
    return len(text.split('. '))


choise = input(""""
Что хотите ввести?
1: подсчета частоты вхождений символов в текст
2: подсчета количества слов в тексте
3: посчета количества предложений в тексте    
""")
if choise == '1':
    word = input('Введите слово: ')
    print(freq_word(word))

if choise == '2':    
    sentence = input('Введите предложение: ')
    print(f'Слов в предложении: {freq_sentence(sentence)}')

if choise == '3':
    text = input('Введите текст: ')
    print(f'Предложений в тексте: {freq_text(text)}')

#Написать программу подсчета частоты вхождений символов в текст с использованием lambda. #########################################
freq_word = {}

word = input('Введите слово: ')

for i in word: freq_word[i] = (lambda i: freq_word.get(i, 0) + 1)(i)

print(freq_word)

##################################################################################################################################