# Задача 2
# Дана вещественная матрица А(3,4).
# Составить программу подсчета количества элементов матрицы,
# удовлетворяющих условию р1<=a(i,j)<=p2.
# Значения р1 и р2 запрашиваются у пользователя.
the_matrix = [[12, 5, 4, 1],
              [3, 7, 13, 4],
              [5, 12, 5, 1]]


def number_of_items(my_matrix, a, b):
    count = 0
    for i in my_matrix:
        for j in i:
            if a <= j <= b:
                count += 1
    return count


def main():
    p1 = int(input('Enter p1:'))
    p2 = int(input('Enter p2:'))
    print(number_of_items(the_matrix, p1, p2))


if __name__ == '__main__':
    main()
