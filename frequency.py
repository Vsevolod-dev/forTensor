# word = input("Введите слово = ")

# all_freq = {}

# for i in word:
#     if i in all_freq:
#         all_freq[i] += 1
#     else:
#         all_freq[i] = 1

# # результат печати

# print(all_freq)

begin = int(input("Введите начало массива = "))
end = int(input("Введите начало массива = "))

strNum = ''
while begin <= end:
    strNum += str(begin)
    begin += 1

print(strNum)

all_freq = {}

for i in strNum:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# результат печати

print(all_freq)