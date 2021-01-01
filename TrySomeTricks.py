from RSA import RSA_code
from AES_file import AES_code
from XOR import XOR_code

print('''Привет! Это текстовая версия "Шифратора". 
Что зашифровать или расшифровать?
- Сообщение
- Файл''')

choice = input().lower()

if choice.startswith('с'):
    print('''Какой алгоритм шифрования применить:
- Синхронный
- Асинхронный''')
    choice = input().lower()
    if choice.startswith('а'):
        print('''Вид криптографического шифра:
- RSA''')
        if input().lower().startswith('r'):
            RSA_code()
    elif choice.startswith('с'):
        print('''Вид криптографического шифра:
- XOR''')
        if input().lower().startswith('x'):
            XOR_code()
elif choice.startswith('ф'):
    print('''Какой алгоритм шифрования применить:
- Синхронный''')
    choice = input().lower()
    if choice.startswith('с'):
        print('''Вид криптографического шифра:
- AES''')
        if choice.startswith('a'):
            print(AES_code())
