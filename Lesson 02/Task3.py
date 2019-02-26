# Написать программу “Калькулятор“, которая умеет выполнять простые арифметические операции
# (сложение, вычитание, умножение, деление) над двумя числами.
# Числа запрашиваются у пользователя “Enter first operand:“, “Enter second operand:“.
# Операция также запрашивается “Enter operator:” где указывается ‘+’, ‘-’, ‘/’, ‘*’.
# Результат вывести в виде, например, “Result: 12".
# Если пользователь ввел отличную от разрешенных операцию, результат должен быть ‘Result: NaN’.

a = input('Enter first operand:')


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


if isint(a) or isfloat(a):
    print('Operand:', a, 'is OK')
    b = input('Enter second operand:')
    if isint(b) or isfloat(b):
        print('Operand:', b, 'is OK')
        op = input('Enter operator:')
        if op in ('*', '/', '+', '-'):
            print('OK')
            if op == '*':
                c = int(a) * int(b)
                print('Result:', c)
            elif op == '/':
                c = int(a) / int(b)
                print('Result:', c)
            elif op == '-':
                c = int(a) - int(b)
                print('Result:', c)
            elif op == '+':
                c = int(a) + int(b)
                print('Result:', c)
        else:
            print('Wrong operator')
    else:
        print('Result: NaN')
else:
    print('Result: NaN')
