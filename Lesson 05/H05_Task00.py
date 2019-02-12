# Задача 0
# Дан список А1..AN. Найти элемент,
# который чаще всего встречается,
# вывести его значение и количество повторений.

check_list = [1, 'a', 11, 'b', 'c', '2', 'h', '2', 'g', '4', '4',
              'D', '2', 'ab', 23, 'ad', '42', 'ab', 'AB', 'ab',
              'q', 'd', 'ab', 'c32', '1', 1, 'w34', 41, 'we']


def select_second_element(a):
    return a[1]


def form_item_repeats(my_list):
    repeat_list = []
    for i in my_list:
        counter = 0
        for j in my_list:
            if i == j:
                counter += 1
        repeat_item = [i, counter]
        if repeat_item not in repeat_list:
            repeat_list.append(repeat_item)
    return repeat_list


def main():
    print(*sorted(form_item_repeats(check_list), key=select_second_element, reverse=True)[0])


if __name__ == '__main__':
    main()
