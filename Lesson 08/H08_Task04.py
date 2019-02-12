# Задача 4
# Реализовать программу, которая выводит содержимое каталога в файловой системе.
# Путь к каталогу запрашивается у пользователя.
import os
from os import path

directory = input('Input path:')
if path.isdir(directory):
    for i in os.scandir(path.normpath(directory)):
        print(i.name)
else:
    print('Invalid directory name!')

