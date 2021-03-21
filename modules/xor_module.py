def cryption(msg, key):                  
    """Функция шифрования и дешифрования    

    Keyword arguments:
    msg -- наше сообщение(или шифрованное сообщение)
    key -- наш ключ

    return:
    crypt -- зашифрованное/расшифрованное сообщение
    """
    crypt = ""

    # Итерация по слову и исключающее или посимвольно с ключом.
    for i in range(len(msg)):
        crypt += chr(ord(msg[i]) ^ ord(key[i % len(key)]))

    return crypt