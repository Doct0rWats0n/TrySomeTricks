from RSA import *

print('''Привет! Это текстовая версия "Шифратора". 
Что зашифровать?
- Сообщение
- Файл''')

if input().lower().startswith('с'):
    print('''Какой алгоритм шифрования применить:
- Синхронный
- Асинхронный''')
    if input().lower().startswith('а'):
        print('''Вид криптографического шифра:
- RSA''')
        if input().lower().startswith('r'):
            rsa_code()
