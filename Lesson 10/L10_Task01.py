import json


def decor(f):
    def wrapper():
        to_write = f()
        if isinstance(to_write, (tuple, list, dict)):
            print('JSON', type(to_write))
            with open('results.json', 'a') as f_json:
                json.dump(to_write, f_json)
        elif isinstance(to_write, (str, int, float)):
            print('STR', type(to_write))
            with open('results.txt', 'a') as f_str:
                f_str.write(to_write)
        else:
            print(type(to_write))

    return wrapper

@decor
def str_out():
    my_string = 'Hello! This is string!!'
    return my_string


@decor
def tuple_out():
    my_tuple = ('Tuple VAL1', 'Tuple VAL2')
    return my_tuple

str_out()


tuple_out()

