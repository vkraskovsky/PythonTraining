# Задача 0
# Создать текстовый файл, записать в него построчно данные,
# которые вводит пользователь. Окончанием ввода пусть служит пустая строка.

from time import ctime


def create_file(my_time, file_test):
    user_info = input('Enter your info:')
    if user_info != '':
        file_test.write(str(user_info) + ' - ' + my_time + '\n')
        create_file(my_time, file_test)


def main():
    my_time = str(ctime())
    print(my_time)
    my_filename = ('/home/slava/dev/Temp/H08_Task00/my_file_' + my_time + '.txt')
    print(my_filename)
    with open(my_filename, "a+") as file_test:
        create_file(my_time, file_test)
    # ---===Variant with while===---
    # while True:
    #     user_info = input('Enter your info:')
    #     if user_info != '':
    #         file_test.write(str(user_info) + ' - ' + my_time + '\n')
    #     else:
    #         break


if __name__ == '__main__':
    main()
