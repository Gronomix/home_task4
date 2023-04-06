'''На основе файла example.csv создать JSON  с помощью Pandas.
Получить среднее значение для каждой колонки файла.
'''


import pandas as pd

csv_file = pd.read_csv('exampl.csv')

print(csv_file['Age  '].mean(axis=3))

csv_file.to_json('example.json')


