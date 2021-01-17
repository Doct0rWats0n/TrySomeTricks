def XOR_code():
    word, key = list(input("Введите сообщение\n")), input("Введите ключ шифрования\n")

    if key.isalpha():
        key_values = 0
        for letter in key:
            key_values += ord(letter)

    for letter in range(len(word)):
        try:
            word[letter] = chr(ord(word[letter]) ^ int(key))
        except ValueError:
            word[letter] = chr(ord(word[letter]) ^ key_values)

    print("Итоговое сообщение:", "".join(word))
