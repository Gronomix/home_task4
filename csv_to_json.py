'''Перевести csv файл в json.'''

import csv
import json

with open('file_csv.csv') as f:
    reader = csv.reader(f)
    next(reader)
    d = dict((rows[0], rows[1:]) for rows in reader)

with open('file_csv.json', 'w') as f:
    json.dump(d, f, indent=4)