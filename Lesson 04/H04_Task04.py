# Задача 4
# Начальный вклад в банке равен 1000 BYN. Через каждый месяц размер вклада увеличивается на P-процентов
# (P - вещественное число, 0 < P < 25). Значение P запрашивается у пользователя.
# По данному P определить, через сколько месяцев размер вклада превысит 1100 BYN
# и вывести найденное количество месяцев и итоговый размер вклада.


VKLAD_START = 1000


def check_num(a):
    try:
        b = float(a)
        return True
    except ValueError:
        return None


# def check_num1(a):
#     num_list={'0','1','2','3','4','5','6','7','8','9','.'}
#     num_draft=set(list(a))
#     if num_draft.issubset(num_list):
#         if list(a)[0]!='.' and list(a)[-1]!='.':
#             if a.count('.')<=1:
#                 print('Value is correct!')
#                 return True


def count_proc(a, b):
    month_count = 1
    while float(a) < 1100:
        a = float(a) + float(a) * float(b) / 100
        month_count += 1
    print('Your deposit will be equal %.2f' % a, 'in a', month_count, 'month(s)!')


def get_proc():
    while True:
        proc = input('Enter % value:')
        if check_num(proc) and 0 < float(proc) < 25:
            break
        print('Wrong % value!')
    print('Your deposit is', VKLAD_START, 'and % is', float(proc))
    a = float(proc)
    return a


def main():
    vklad_start = 1000
    count_proc(vklad_start, get_proc())


if __name__ == '__main__':
    main()
