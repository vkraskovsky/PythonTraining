def check_num(a):
    num_list = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    num_draft = set(list(a))
    if num_draft.issubset(num_list):
        return True


def my_sum(a, b, *args):
    if check_num(str(a)) and check_num(str(b)):
        if args and min(args) != 0:
            d = 1
            for i in args:
                d *= i
            c = a + b + d / min(args)
        else:
            c = a + b
        return c


print(my_sum(1, 2, 4, 5, 6, 5))
