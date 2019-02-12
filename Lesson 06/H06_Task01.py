# Задача 1*
# Написать программу нахождения простых чисел, используя решето Эратосфена.
# Для каждой из пользовательских функций написать функцию-тест.

from math import sqrt


def simple_nums(n):
    my_sieve = set(range(2, n))
    for i in range(2, int(sqrt(n)) + 1):
        if i in my_sieve:
            my_sieve -= set(range(2 * i, n, i))
    return my_sieve


def test_simple_nums():
    assert simple_nums(10) == {2, 3, 5, 7}


def main():
    test_simple_nums()
    print(simple_nums(int(input('Enter number'))))


if __name__ == '__main__':
    main()
