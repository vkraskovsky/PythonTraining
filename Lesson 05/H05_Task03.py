# Задача 3
# Реализовать программу с базой учащихся группы.
# Записи по учащемуся: имя, фамилия, пол, возраст.
# Программа должна предусматривать поиск по одному или нескольким полям базы.
# Результат выводить в удобочитаемом виде с порядковым номером записи.

student_list = [['Ivan', 'Ivanov', 'Male', '15'],
                ['Ivanka', 'Ivanova', 'Female', '18'],
                ['Piotr', 'Petrov', 'Male', '18'],
                ['Petra', 'Petrova', 'Female', '16'],
                ['Elena', 'Kravtsova', 'Female', '14'],
                ['Pavel', 'Smirnov', 'Male', '17'],
                ['Alex', 'Vlasov', 'Male', '18']]

args = input('Enter search criteria:')


def search_student(student_list, args):
    marker = 0
    for i in range(len(student_list)):
        if set(args.split()).issubset(set(student_list[i])):
            print(i, *student_list[i])
            marker = 1
    if marker == 0:
        print('No results found!')


def main():
    search_student(student_list, args)


if __name__ == '__main__':
    main()
