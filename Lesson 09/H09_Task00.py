# Задача 0
# Реализовать программу с базой учащихся группы.Записи по учащемуся: имя, фамилия, пол, возраст.
# Программа должна предусматривать поиск по одному или нескольким полям базы.
# Результат выводить в удобочитаемом виде с порядковым номером записи.
# База должна быть сохранена в файле в формате `json`. Поиск так же должен быть реализован по файлу.

import json

student_file = '/home/slava/dev/Temp/H09_Task00/students.json'
args = input('Enter search criteria:')
count = 0
with open(student_file) as student_json:
    student_data = json.load(student_json)
for student in student_data:
    if set(args.split()).issubset(set(student.values())):
        count += 1
        print(count, *student.values())
if count == 0:
    print('No results found!')


