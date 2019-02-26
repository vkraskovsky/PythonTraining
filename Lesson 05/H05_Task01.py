# Задача 1
# Дана целая матрица А(N,N).
# Составить программу подсчета среднего арифметического значения элементов матрицы.
the_matrix = [[2, 5, 4, 1, 4],
              [3, 7, 3, 4, 2],
              [5, 2, 5, 1, 22],
              [4, 6, 5, 3, 5],
              [10, 25, 3, 1, 6]]


def number_of_items(my_matrix):
    count = 0
    for i in my_matrix:
        for j in i:
            count += 1
    return count


def sum_of_items(my_matrix):
    my_sum = 0
    for i in my_matrix:
        my_sum += sum(i)
    return my_sum


def main():
    print(sum_of_items(the_matrix))
    print(number_of_items(the_matrix))
    print(sum_of_items(the_matrix) / number_of_items(the_matrix))


if __name__ == '__main__':
    main()
