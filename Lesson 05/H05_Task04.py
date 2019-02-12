# Задача 4*
# Дана квадратная матрица А(N,N).
# Составить программу подсчета количества положительных элементов,
# расположенных выше главной диагонали.
the_matrix = [[12, -5, 4, -1, 5],
              [3, 7, -13, -4, -2],
              [5, 12, -5, 1, -25],
              [-1, -4, 6, 5, -15],
              [12, 12, -32, -4, 5]]


def number_of_items(my_matrix):
    count = 0
    count_i = 0
    for i in my_matrix:
        for j in i[(count_i + 1):]:
            if j <= 0:
                count += 1
        count_i += 1
    return count


def main():
    print(number_of_items(the_matrix))


if __name__ == '__main__':
    main()
