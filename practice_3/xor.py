from modules import xor_module

msg = input("Введите слово = ")
key  = input("Введите ключ = ")

encmsg = xor_module.cryption(msg, key)

# Открытие файла и чтение из него.
with open("test.txt", "w") as file:
    file.write(encmsg)

print(encmsg)

# Открытие файла и чтение из него, функция шифрования.
with open("test.txt", "r") as file:
    for line in file:
        decmsg = xor_module.cryption(encmsg, key)

print(f'Декодированное сообщение = {decmsg}')