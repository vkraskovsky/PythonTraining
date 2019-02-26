# Задача 3
# Реализовать программу с базой учащихся группы (данные хранятся в файле).
# Записи по учащемуся: имя, фамилия, пол, возраст.
# Программа должна предусматривать поиск по одному или нескольким полям базы.
# Результат выводить в удобочитаемом виде с порядковым номером записи.


def main():
    student_list_file = '/home/slava/dev/Temp/H08_Task03/student_list.txt'
    args = input('Enter search criteria:')
    count = 0
    with open(student_list_file, 'r') as students:
        for student in students.readlines():
            if set(args.split()).issubset(set(student.split())):
                count += 1
                print(count, student)
        if count == 0:
            print('No results found!')


if __name__ == '__main__':
    main()
