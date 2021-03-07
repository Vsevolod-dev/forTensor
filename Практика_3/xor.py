msg = input("Введите слово = ")
key  = input("Введите ключ = ")

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

encmsg = encryption(msg, key)

with open("/home/admin/Документы/forTensor/Практика_3/test.txt", "w") as file:
    file.write(encmsg)

print(encmsg)

with open("/home/admin/Документы/forTensor/Практика_3/test.txt", "r") as file:
    for line in file:
        decmsg = decryption(encmsg, key)

print(decmsg)