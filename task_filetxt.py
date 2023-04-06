'''Создать файл, прочесть его, вывести количество строк файла.
Создать файл, заменить в этом файле строку.
Удалить строку из файла по ее индексу.
Вставить строку в указанную позицию файла.
'''

import random

data = (f"{[random.randint(0, 20) for elem in range(5)]} \n" + f'"a", sdd , ggg, s, d, f, rrr \n')

with open("some_file.txt", "w") as file:
    writ = file.write(data)
    write = file.write(data + f"\n, 21123123123\n, sdfsdfsdff")



with open("some_file.txt", "r+") as file:
    #print(file.read())
    line = file.readlines()
    print(line)
    line[4] = f'This is new line'
    for elem in line:
        print(elem)
    print(f"Количество сtрок в файле: {len(line)}")


with open("some_file.txt", 'w+') as file:
    file.writelines(line)
    file.seek(4)
    file.write('----NEW______')
    line1 = file.readlines()
    file.seek(17)
    line1 = file.writelines(' Good news, ')









