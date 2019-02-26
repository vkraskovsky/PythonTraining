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


def number_of_items(my_matrix):
    count = 0
    for i in my_matrix:
        for j in i:
            count += 1
    return count


def number_of_items_in(my_matrix, a, b):
    count = 0
    for i in my_matrix:
        for j in i:
            if a <= j <= b:
                count += 1
    return count


def sum_of_items(my_matrix):
    my_sum = 0
    for i in my_matrix:
        my_sum += sum(i)
    return my_sum


def search_student(student_list, args):
    marker = 0
    for i in range(len(student_list)):
        if set(args.split()).issubset(set(student_list[i])):
            print(i, *student_list[i])
            marker = 1
    if marker == 0:
        print('No results found!')


def number_of_items_d(my_matrix):
    count = 0
    count_i = 0
    for i in my_matrix:
        for j in i[(count_i + 1):]:
            if j <= 0:
                count += 1
        count_i += 1
    return count

