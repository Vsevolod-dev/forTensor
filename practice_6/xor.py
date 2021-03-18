def encryption(msg, key):
    crypt = ""

    for i in range(len(msg)):
        crypt += chr(ord(msg[i]) ^ ord(key[i % len(key)]))

    return crypt

def decryption(msg, key):
    decrypt = ""

    for i in range(len(msg)):
        decrypt += chr(ord(msg[i]) ^ ord(key[i % len(key)]))
        
    return decrypt

with open("test.txt", "r", encoding='utf-8') as file: 
   msg = file.read()

print(msg)

key = input("Введите ключ = ")

encmsg = encryption(msg, key)

with open("test.txt", "w") as file: 
    file.write(encmsg)

#print(encmsg) # сообщение скорее всего не выдаст, или не полностью, лучше смотреть в созданном файле

with open("test.txt", "r") as file:
    for line in file:
        decmsg = decryption(encmsg, key)

print(f'Декодированное сообщение = {decmsg}')