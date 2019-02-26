# Задача 3
# Вводятся строки. Определить самую длинную строку и вывести ее номер на экран.
# Если самая длинная строка повторяется несколько раз, то вывести номера всех таких строк.


def get_list_of_strings():
    list_of_strings = []
    while True:
        string_add = input('Add string. Press "e" to stop:')
        if string_add == 'e':
            break
        else:
            list_of_strings.append(string_add)
    print('Your strings:', list_of_strings)
    return list_of_strings


def find_max_string(a):
    max_string = max(a, key=len)
    for i, j in enumerate(a):
        if len(j) == len(max_string):
            print(i, j)


def main():
    find_max_string(get_list_of_strings())


if __name__ == '__main__':
    main()
