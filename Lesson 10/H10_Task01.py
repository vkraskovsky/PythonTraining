# Задача 1
# Реализовать программу, которая отображает дерево каталогов.
# Путь к целевому каталогу запрашивается у пользователя. В программе не должно использоваться циклов.
# Вывод результата программы должен быть следующего вида:
# |__ Folder 1
# |___ Folder 2
# |___ File 2.1
# |___ File 2.2
# |__ File 1.1
# |__ File 1.2
import os
from os import path


def print_tree1(directory):
    if path.isdir(directory):
        tree = os.walk(directory)
        for root, dirs, files in tree:
            for d in dirs:
                print(path.join(root, d))
            for f in files:
                print(path.join(root, f))
    else:
        print('Wrong path!')


def print_tree2(directory):
    if path.isdir(directory):
        for dir_list in os.listdir(directory):
            dir_path = path.join(directory, dir_list)
            if path.isfile(dir_path):
                print('|__', dir_list)
            if path.isdir(dir_path):
                print('|__', dir_list)
                print_tree2(dir_path)

    else:
        print('Wrong path!')


def main():
    # my_directory = input("Enter path:")
    my_directory = '/home/slava/dev/Temp'
    print_tree2(my_directory)


if __name__ == '__main__':
    main()
