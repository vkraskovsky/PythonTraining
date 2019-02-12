def input_string():
    str_draft = input('Enter string containing one number:')
    num_draft = input('Enter number:')
    return str_draft, num_draft


def is_string_valid(a):
    nums_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    if len(set(a).intersection(nums_set)) == 1:
        return True


def find_intersection(a, b):
    c = set(a).intersection(set(b))
    return c


values_to_check = input_string()[0:2]
print('values_to_check =', values_to_check, 'type', type(values_to_check))
if is_string_valid(values_to_check[0]):
    if is_string_valid(values_to_check[1]):
        inter = find_intersection(values_to_check[0], values_to_check[1])
        if is_string_valid(inter):
            print('Your number is ', str(list(inter)[0]))
        else:
            print('No intersections...')
    else:
        print('Wrong Number!!!')
else:
    print('Wrong String!!!')

# b = is_string_valid(input_string()[0:])
