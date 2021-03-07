# # XOR для шифрования/расшифровки
# def xor_cipher( msg, key ):
#     encript_str = ""
#     key_itr = 0
#     for i in range(len(msg)):
#         temp = ord(msg[i]) ^ ord(key[key_itr])
 
#         encript_str += bin(temp)[2:].zfill(2)
#         key_itr += 1
#         if key_itr >= len(key):
#             key_itr = 0
    
#     chr
#     return encript_str

# def cipher_decryption(msg, key):
#     bin_to_uni = ""
#     for i in range(0, len(msg), 2):
#         bin_to_uni += bytes.frombin(msg[i:i+2]).decode('utf-8')

#     decrypt_text = ""
#     key_itr = 0
#     for i in range(len(bin_to_uni)):
#         temp = ord(bin_to_uni[i]) ^ ord(key[key_itr])
#         decrypt_text += chr(temp)
#         key_itr += 1
#         if key_itr >= len(key):
#             key_itr = 0
#     return decrypt_text

msg = 'hello'#input("Введите слово = ")
key  = "s"#input("Введите ключ = ")

crypt = ""
itr = 0
while len(key) < len(msg):
    key += key
print(key)
for i in msg:
    crypt += chr(ord(i)^ord(key[itr]))
    itr += 1
    if itr >= len(msg):
        key_itr = 0
print(crypt)

msg = ""
itr = 0
for i in crypt:
    msg += chr(ord(i)^ord(key[itr]))
    itr += 1
print(msg)

# # msg = b(msg)
# # key = b(key)

# print(xor_cipher(msg, key))
# print(cipher_decryption(xor_cipher(msg, key), key))
# # bmsg = ''.join(format(ord(i), 'b') for i in msg)
# # bkey = ''.join(format(ord(i), 'b') for i in key)

# # print(bin(msg))

# # print(msg^key)

