import rsa

from rsa import PrivateKey, PublicKey


def rsa_code():
    print('Зашифровать, расшифровать или сгенерировать ключи?')

    what_to_do = input().lower()

    if what_to_do.startswith('з'):
        print('Введите открытый ключ шифрования')
        a, b = [int(i) for i in input().split(', ')]
        public_key = PublicKey(a, b)
        print('Введите сообщение для зашифровки')
        word = input().encode('utf-8')
        print('''Введите имя файла для сообщения''')
        fileName = input() + '.txt'
        crypto_word = rsa.encrypt(word, public_key)
        with open(fileName, "wb") as file:
            file.write(crypto_word)
            print('Сообщение было сохранено')
    elif what_to_do.startswith('р'):
        print('Введите закрытый ключ шифрования')
        a, b, c, d, e = [int(i) for i in input().split(', ')]
        private_key = PrivateKey(a, b, c, d, e)
        print('Введите название файла с сообщением')
        fileName = input()
        with open(fileName, "rb") as file:
            decrypt = rsa.decrypt(file.read(), private_key)
        print(decrypt.decode('utf-8'))
    elif what_to_do.startswith('с'):
        print('Записать в файл? (Да/Нет)')
        word = input().lower()
        public_key, private_key = rsa.newkeys(512)
        if word.startswith('д'):
            public_key, private_key = str(public_key), str(private_key)
            fileName = "keys.txt"
            with open(fileName, "w") as file:
                file.write(public_key)
                file.write('\n')
                file.write(private_key)
                print('Файл %s сохранен' % fileName)
        print(public_key, private_key, sep='\n')
