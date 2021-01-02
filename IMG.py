from stegano import exifHeader


def IMG_code():
    what_to_do = input('Скрыть текст или прочитать?\n').lower()
    if what_to_do.startswith('с'):
        original = input('Укажите путь до изображения в формате jpg. Пример: /home/user/photo.jpg\n')
        copy = input('''Укажите путь до нового изображения. Создавать отдельно не нужно. Пример: 
/home/user/new_photo.jpg\n''')
        text = input('Введите сообщение, которое хотите скрыть\n')
        exifHeader.hide(original, copy, text)
        print('Изображение создано')
    elif what_to_do.startswith('п'):
        photo = input('Укажите путь до изображения в формате jpg\n')
        print(exifHeader.reveal(photo).decode())
