# Задача 1
# Реализовать программу с базой учащихся группы (данные хранятся в файле).
# Записи по учащемуся должны быть представлены отдельным классом с полями: имя, фамилия, пол, возраст.
# Программа должна предусматривать поиск по одному или нескольким полям базы.
# Результат выводить в удобочитаемом виде с порядковым номером записи.
# Скрипт программы должен принимать параметр, который определяет формат хранения и реализации БД:
# в текстовом файле с определенной структурой; в файле json.
import json
import argparse

FILE_NAME_JSON = '/home/slava/dev/Temp/H11_Task00/students.json'
FILE_NAME_TXT = '/home/slava/dev/Temp/H11_Task00/students.txt'


class Search:
    def search_student(self, args):
        if args == set():
            return False
        else:
            return args.issubset(set(self.__dict__.values()))


class StudentJSON(Search):
    def __init__(self, student_dict):
        self.name = student_dict['name']
        self.surname = student_dict['secname']
        self.gender = student_dict['gender']
        self.age = student_dict['age']

    @staticmethod
    def read():
        with open(FILE_NAME_JSON, 'r') as students_json:
            students_data = json.load(students_json)
            for student_dict in students_data:
                yield student_dict


class StudentTXT(Search):
    def __init__(self, student_list):
        self.name = student_list[1]
        self.surname = student_list[0]
        self.gender = student_list[2]
        self.age = student_list[3]

    @staticmethod
    def read():
        for line in open(FILE_NAME_TXT, 'r'):
            student_list = line.strip().split()
            yield student_list


# class Student:
#     def __init__(self, name, surname, gender, age):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.age = age
#
#         
# class StudentUtil:
#     @staticmethod
#     def read_json():
#         with open(FILE_NAME_JSON, 'r') as students_json:
#             students_data = json.load(students_json)
#             # print(students_data)
#             return students_data, 'json'
#
#     @staticmethod
#     def read_txt():
#         students_data = []
#         for line in open(FILE_NAME_TXT, 'r'):
#             students_data.append(line.strip().split())
#         # print(students_data)
#         return students_data, 'txt'
#
#     @staticmethod
#     def build_students(student_data_, build_format):
#         student_object_list = []
#         if build_format == 'json':
#             for student_dict in student_data_:
#                 student_object = Student(student_dict['name'], student_dict['secname'],
#                                          student_dict['gender'], student_dict['age'])
#                 student_object_list.append(student_object)
#                 # print(student_object_list, student_object.name)
#             return student_object_list
#         elif build_format == 'txt':
#             for student_list in student_data_:
#                 student_object = Student(student_list[1], student_list[0], student_list[2], student_list[3])
#                 student_object_list.append(student_object)
#                 # print(student_object_list, student_object.name)
#             return student_object_list
#
#     @staticmethod
#     def search_student(student_object_list_):
#         search_args = input('Enter search criteria:')
#         count = 0
#
#         for student_object in student_object_list_:
#             student_values = student_object.__dict__.values()
#             if set(search_args.split()).issubset(set(student_values)):
#                 count += 1
#                 print(count, *student_values)
#         if count == 0:
#             print('No results found!')


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--text', action='store_const', const=1, help='Text format for the database')
    parser.add_argument('-j', '--json', action='store_const', const=2, help='JSON format for the database')
    # print(parser.parse_args())
    if parser.parse_args().text == 1:
        print('Using TXT format...')
        template = StudentTXT
    elif parser.parse_args().json == 2:
        print('Using JSON format...')
        template = StudentJSON
    else:
        while True:
            par = input('No arguments were given!\n Enter 1 - for TXT, 2 - for JSON.\nYour choice:')
            if par in ('1', '2'):
                if par == '1':
                    print('Using TXT format...')
                    template = StudentTXT
                    break
                elif par == '2':
                    print('Using JSON format...')
                    template = StudentJSON
                    break
                else:
                    print('Wrong choice!')
    search_args = set(input('Enter search criteria:').split())
    count = 0
    for student_item in template.read():
        student = template(student_item)
        if student.search_student(search_args):
            count += 1
            print(count, student.name, student.surname, student.gender, student.age)
    if count == 0:
        print('No results found!')


if __name__ == '__main__':
    main()
