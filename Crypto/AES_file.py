from pyAesCrypt import encryptFile, decryptFile
from os import remove
from os.path import splitext


def AES_code():
    print('Зашифровать или расшифровать файл?')
    mode = input().lower()
    print('Введите имя файла')
    file = input()
    print('Введите пароль')
    password = input()
    bufferSize = 64 * 1024
    if mode.startswith('з'):
        try:
            encryptFile(str(file), str(file) + ".crp", password, bufferSize)
            remove(file)
        except FileNotFoundError:
            return "Файл не найден!"
        else:
            return "Файл %s зашифрован" % file
    elif mode.startswith('р'):
        try:
            decryptFile(str(file), str(splitext(file)[0]), password, bufferSize)
            remove(file)
        except FileNotFoundError:
            return "Файл не найден!"
        except ValueError:
            return "Неверный пароль"
        else:
            return "Файл %s расшифрован!" % file
