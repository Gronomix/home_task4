'''Создать и прочитать CSV файл с помощью Pandas.
Запросить у пользователя данные (имя, фамилия, возраст) и создать файл с этими значениями.


'''

import pandas as pd

df = pd.read_csv('exampl.csv')
print(df)
print(df.head())

name = input('Введите имя ')
sur = input('введите фамилию ')
age = input('Введите возраст ')

men = pd.DataFrame([[name, sur, age]], columns=['Name  ', 'Surname   ', 'Age  '])
men.to_csv('exampl.csv', mode='a', index=False, header=False)