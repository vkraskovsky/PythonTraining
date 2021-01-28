# Задача 0
# Реализовать модуль, содержащий следующие функции декораторы:
# декоратор, позволяющий вместе с результатом функции возвращать время ее работы;
# декоратор, позволяющий записывать время работы функции, имя функции и переданные ей параметры в текстовый файл;
# декоратор, проверяющий типы, переданных декорируемой функции, аргументов.
# декоратор, который кэширует результат работы функции, тем самым обеспечивает единственный вызов функции.
import time
import json
from random import randint


def try_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


# декоратор, позволяющий вместе с результатом функции возвращать время ее работы;


def dec_work_time(func):
    def wrap_work_time(wrap_rows, wrap_columns):
        start_time = time.time()
        matrix = func(wrap_rows, wrap_columns)
        work_time = round(time.time() - start_time, 5)
        return matrix, work_time

    return wrap_work_time


# декоратор, позволяющий записывать время работы функции, имя функции и переданные ей параметры в текстовый файл;


def dec_to_file(func):
    def wrap_to_file(wrap_rows, wrap_columns):
        start_time = time.time()
        func(wrap_rows, wrap_columns)
        work_time = round(time.time() - start_time, 10)
        file_name = '/home/slava/dev/Temp/H10_Task00/dec_to_file.txt'
        with open(file_name, 'a') as results:
            results.write('Function Time: {}, Function Name: {}, \
Function Args: {},{}\n'.format(str(work_time), func.__name__, wrap_rows, wrap_columns))
        return func

    return wrap_to_file


# декоратор, проверяющий типы, переданных декорируемой функции, аргументов.


def dec_check_args(func):
    def wrap_check_args(wrap_rows, wrap_columns):
        if try_int(wrap_rows) and try_int(wrap_columns):
            return func
        else:
            (print('Wrong Values!'))
            raise ValueError

    return wrap_check_args


# декоратор, который кэширует результат работы функции, тем самым обеспечивает единственный вызов функции.


def dec_cache_result(func):

    def wrap_cache_result(*args):
        cache_file = '/home/slava/dev/Temp/H10_Task00/cached_results.json'
        with open(cache_file) as result_json:
            cached_result = json.load(result_json)
        if str(args) in cached_result.keys():
            print('Using cache')
            return cached_result[str(args)]

        else:
            print('New result')
            new_result = func(*args)
            args_keys = str(args)
            cached_result[args_keys] = new_result
            with open(cache_file, 'w') as result_json:
                json.dump(cached_result, result_json)
            return new_result

    return wrap_cache_result


# @dec_work_time
# @dec_to_file
@dec_check_args
def my_func1(rows, columns):
    my_matrix = []
    for i in range(int(rows)):
        my_row = []
        for j in range(int(columns)):
            my_row.append(randint(10, 20))
        my_matrix.append(my_row)
        print(my_row)
    return my_matrix


@dec_cache_result
def my_func2(*args):
    sum_args = 0
    for i in args:
        sum_args += int(i)
    return sum_args


def main():
    my_rows = input('Enter number of rows:')
    my_columns = input('Enter number of columns:')
    my_func1(my_rows, my_columns)
    my_func2(4, 5, 8)


if __name__ == '__main__':
    main()
