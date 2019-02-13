# Для решений задач занятия №5 вынести общие части в модули. Сделать единую точку входа app.py.
# Необходимо реализовать возможность старта выполнения кода одного из заданий сразу после запуска программы,
# а также после его выполнения предоставить возможность выполнить другое задание без повторного запуска программы.
# From task 00
from func_utils import form_item_repeats
from func_utils import select_second_element
# from task 01
from func_utils import number_of_items
from func_utils import sum_of_items
# from task 02
from func_utils import number_of_items_in
# from task 03
from func_utils import search_student
# from task 04
from func_utils import number_of_items_d


def select_task():
    while True:
        task_to_run = input('Select task to run 0 - 4 (s - to stop): ')
        if task_to_run in ['0', '1', '2', '3', '4']:
            print('Running task', task_to_run, '...')
            break
        elif task_to_run == 's':
            print('Ending...')
            break
        else:
            print('Wrong task number!')
    return task_to_run


def my_tasks_run(task_num):
    if task_num == 0:
        # Задача 0
        # Дан список А1..AN. Найти элемент,
        # который чаще всего встречается,
        # вывести его значение и количество повторений.
        check_list = [1, 'a', 11, 'b', 'c', '2', 'h', '2', 'g', '4', '4',
                      'D', '2', 'ab', 23, 'ad', '42', 'ab', 'AB', 'ab',
                      'q', 'd', 'ab', 'c32', '1', 1, 'w34', 41, 'we']
        print(*sorted(form_item_repeats(check_list), key=select_second_element, reverse=True)[0])
    if task_num == 1:
        # Задача 1
        # Дана целая матрица А(N,N).
        # Составить программу подсчета среднего арифметического значения элементов матрицы.
        the_matrix = [[2, 5, 4, 1, 4],
                      [3, 7, 3, 4, 2],
                      [5, 2, 5, 1, 22],
                      [4, 6, 5, 3, 5],
                      [10, 25, 3, 1, 6]]
        print(sum_of_items(the_matrix))
        print(number_of_items(the_matrix))
        print(sum_of_items(the_matrix) / number_of_items(the_matrix))
    if task_num == 2:
        # Задача 2
        # Дана вещественная матрица А(3,4).
        # Составить программу подсчета количества элементов матрицы,
        # удовлетворяющих условию р1<=a(i,j)<=p2.
        # Значения р1 и р2 запрашиваются у пользователя.
        the_matrix = [[12, 5, 4, 1],
                      [3, 7, 13, 4],
                      [5, 12, 5, 1]]
        p1 = int(input('Enter p1:'))
        p2 = int(input('Enter p2:'))
        print(number_of_items_in(the_matrix, p1, p2))
    if task_num == 3:
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
        search_student(student_list, args)
    if task_num == 4:
        # Задача 4*
        # Дана квадратная матрица А(N,N).
        # Составить программу подсчета количества положительных элементов,
        # расположенных выше главной диагонали.
        the_matrix = [[12, -5, 4, -1, 5],
                      [3, 7, -13, -4, -2],
                      [5, 12, -5, 1, -25],
                      [-1, -4, 6, 5, -15],
                      [12, 12, -32, -4, 5]]
        print(number_of_items_d(the_matrix))


def main():
    while True:
        my_task = (select_task())
        if my_task in ['0', '1', '2', '3', '4']:
            my_tasks_run(int(my_task))
        else:
            break


if __name__ == '__main__':
    main()
