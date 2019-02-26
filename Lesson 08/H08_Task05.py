# Задача 5*
# Реализовать программу, позволяющую осуществлять управление файлами:
# копирование, создание, удаление, переименование.
# Необходимо предусмотреть возможность смен директории.
# Изначально используется текущий каталог запуска скрипта программы.
import os
import shutil
from os import path


def ls():
    for i in os.scandir(path.normpath(os.curdir)):
        print(i.name)


def cd(dst):
    if path.isdir(dst):
        os.chdir(path.normpath(dst))
        print('OK')
    else:
        print('The directory doesn\'t exist')


def cp(src, dst):
    if path.isfile(src):
        shutil.copy(src, dst)
        print('File copied!')
    else:
        print('The file doesn\'t exist')


def mv(src, dst):
    if path.isfile(src):
        os.rename(path.normpath(src), path.normpath(dst))
        print('File moved!')
    else:
        print('The file doesn\'t exist')


def main():
    commands = ('ls', 'cd', 'cp', 'touch', 'mv', 'rm', 'pwd', 'exit')
    while True:
        args = input('Run command:').split()
        if args[0] in commands:
            if args[0] == 'ls':
                ls()
            elif args[0] == 'cd' and len(args) == 2:
                cd(args[1])
            elif args[0] == 'cp' and len(args) == 3:
                cp(args[1], args[2])
            elif args[0] == 'touch' and len(args) == 2:
                (lambda name: open(path.normpath(name), 'w').close())(args[1])
                print('File created!')
            elif args[0] == 'mv' and len(args) == 3:
                mv(args[1], args[2])
            elif args[0] == 'rm' and len(args) == 2:
                (lambda name: os.remove(path.normpath(name)))(args[1]) if path.isfile(args[1]) else print(
                    'The file doesn\'t exist')
            elif args[0] == 'pwd' and len(args) == 1:
                print(os.getcwd() + '/')
            elif args[0] == 'exit' and len(args) == 1:
                print('Bye')
                break
            else:
                print('Wrong command or arguments!!!')
        else:
            print('Wrong command or arguments!!!')


if __name__ == '__main__':
    main()
