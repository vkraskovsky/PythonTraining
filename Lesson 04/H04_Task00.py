# Задача 0
# Написать программу, которая предлагает пользователю ввести список чисел,
# после чего  запрашивает число для которого нужно посчитать сколько раз оно встречается в списке.


def check_num(a):
    num_list = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    num_draft = set(list(a))
    if num_draft.issubset(num_list):
        return True


def get_list():
    num_list = []
    list_len = input('Enter list length:')
    if list_len != '0' and check_num(list_len):
        #    print('if Value is correct!')
        i = 0
        while i < (int(list_len)):
            num_add = input('Add number. Press "e" to stop:')
            if num_add == 'e':
                break
            elif check_num(num_add):
                num_list.append(num_add)
                print(i + 1, num_list)
                i += 1
            else:
                print('Wrong number format!')
                print('i stays:', i)
        return num_list
    else:
        print('Wrong length format!')


def get_num():
    while True:
        num_search = input('Enter number to search:')
        if check_num(num_search):
            break
        else:
            print('Wrong number format!')
    return num_search


def count_num_in_list(a, b):
    my_list = a
    my_num = b
    count = 0
    for i in my_list:
        if my_num == i:
            count += 1
    return count


def main():
    print('Your number found in your list', count_num_in_list(get_list(), get_num()))


if __name__ == '__main__':
    main()
