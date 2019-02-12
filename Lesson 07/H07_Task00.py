# Напишите программу, содержащую описание стека и моделирующую работу стека, реализовав все указанные здесь методы.
# Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию.
# После выполнения каждой команды программа должна вывести одну строчку.
# Возможные команды для программы:
#
# Команда Описание
# push n  Добавить в стек число n (значение n задается после команды). Программа должна вывести ok.
# pop     Удалить из стека последний элемент. Программа должна вывести его значение.
# back    Программа должна вывести значение последнего элемента, не удаляя его из стека.
# size    Программа должна вывести количество элементов в стеке.
# clear   Программа должна очистить стек и вывести ok.
# exit    Программа должна вывести bye и завершить работу.
#
# Входные данные:
# Команды управления стеком вводятся в описанном ранее формате по 1 на строке.
# Гарантируется, что набор входных команд удовлетворяет следующим требованиям:
# максимальное количество элементов в стеке в любой момент не превосходит 100,
# все команды pop и back корректны, то есть при их исполнении в стеке содержится хотя бы один элемент.


def isint(num_val):
    try:
        int(num_val)
        return True
    except ValueError:
        print('Wrong Value!')
        return False


def stack_len(stack_list):
    if len(stack_list) < 100:
        return True
    else:
        print('Stack is full!')
        return False


def push(value, stack_list):
    if isint(value):
        if stack_len(stack_list):
            stack_list.append(value)
            print('ok')


def pop(stack_list):
    if len(stack_list) != 0:
        stack_list.pop()
    else:
        print('Empty stack!!!')


def back(stack_list):
    if len(stack_list) != 0:
        print('The last element is:', stack_list[-1])
    else:
        print('Empty stack!!!')


def size(stack_list):
    print(len(stack_list))


def clear(stack_list):
    stack_list.clear()
    print('ok')


def exit_():
    print('Bye')


def main():
    main_stack = []
    commands = ('push', 'pop', 'back', 'size', 'clear', 'exit')
    while True:
        args = input('Run command:').split()
        if (args[0] == commands[0] and len(args) == 2) or (args[0] in commands[1:] and len(args) == 1):
            if args[0] == 'push':
                push(args[1], main_stack)
            elif args[0] == 'pop':
                pop(main_stack)
            elif args[0] == 'back':
                back(main_stack)
            elif args[0] == 'size':
                size(main_stack)
            elif args[0] == 'clear':
                clear(main_stack)
            else:
                print('bye')
                break
        else:
            print('Wrong command or arguments!!!')


if __name__ == '__main__':
    main()
