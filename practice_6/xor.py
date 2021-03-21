from modules import xor_module

# Открытие файла и чтение из него.
with open("test.txt", "r", encoding='utf-8') as file: 
   msg = file.read()

print(msg)

key = input("Введите ключ = ")

encmsg = xor_module.cryption(msg, key)

# Открытие файла и запись из него.
with open("test.txt", "w") as file: 
    file.write(encmsg)

# Открытие файла и чтение из него, функция шифрования.
with open("test.txt", "r") as file:
    for line in file:
        decmsg = xor_module.cryption(encmsg, key)

print(f'Декодированное сообщение = {decmsg}')