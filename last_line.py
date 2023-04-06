'''Напишите программу, которая будет открывать определенный файл file и выводить на печать построчно последние строки
в количестве lines (на всякий случай проверим, что задано положительное целое число).'''


def read_last(lines, file):
    try:
        if lines > 0:
            with open(file, encoding='utf-8') as text:
                file_lines = text.readlines()[-lines:]
            for line in file_lines:
                print(line.strip())
            else:
                print('Количество строк может быть только целым положительным')
    except ValueError:
        print("Количество строк не может быть отрицательным")


read_last(2, 'article.txt')

read_last(3, 'article.txt')

read_last(-5, 'article.txt')

read_last(-10, 'article.txt')