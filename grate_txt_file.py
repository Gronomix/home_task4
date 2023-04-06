'''Напишите программу в которой создается текстовый файл. Имя файла вводится пользователем.
Текст для файла вводится пользователем. При записи текста в файл все маленькие буквы заменяются на большие.
'''

with open(input('Введите имя файла '), 'w+', encoding='utf-8') as file:
    file.write(input('Введите любую строку: ').upper())
    line = file.readlines()
    leng = int(len(line))
    while leng < 6:
        file.write(input('Введите любую строку: '.upper()))
        print(file.readlines())
        print(leng)
        break


