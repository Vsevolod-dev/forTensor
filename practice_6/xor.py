def encryption(msg, key):
    crypt = ""
    itr = 0

    while len(key) < len(msg):
        key += key

    for i in msg:
        crypt += chr(ord(i) ^ ord(key[itr]))
        itr += 1
    return crypt

def decryption(msg, key):
    decrypt = ""
    itr = 0

    while len(key) < len(msg):
        key += key

    for i in msg:
        decrypt += chr(ord(i)^ord(key[itr]))
        itr += 1
    return decrypt

with open("test.txt", "r", encoding='utf-8') as file: 
   msg = file.read()

print(msg)

key = input("Введите ключ = ")

encmsg = encryption(msg, key)

with open("test.txt", "w") as file: 
    file.write(encmsg)

print(encmsg) # сообщение скорее всего не выдаст, или не полностью, лучше смотреть в созданном файле

with open("test.txt", "r") as file:
    for line in file:
        decmsg = decryption(encmsg, key)

print(f'Декодированное сообщение = {decmsg}')