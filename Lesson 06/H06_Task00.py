# Задача 0
# Написать программу, запрашивающую у пользователя строку с текстом и разделитель.
# Необходимо вывести список слов с их длиной в начале слова, например, 5hello.
# Для каждой из пользовательских функций написать функцию-тест.


def form_my_list(my_string, my_sep):
    my_list = my_string.split(my_sep)
    final_list = []
    for i in my_list:
        final_list.append((lambda x: str(len(x)) + x)(i))
    return final_list


def test_form_my_list():
    assert form_my_list('ab!abc', '!') == ['2ab', '3abc']


def main():
    entered_string = input('Enter your string:')
    while True:
        entered_sep = input('Enter your separator')
        if entered_sep not in entered_string:
            print('Wrong separator!')
        else:
            break
    test_form_my_list()
    print(*form_my_list(entered_string, entered_sep))


if __name__ == '__main__':
    main()
