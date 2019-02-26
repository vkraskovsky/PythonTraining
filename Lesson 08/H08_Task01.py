# Задача 1
# В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество в ней символов и слов.

my_file = '/home/slava/dev/Temp/H08_Task01/H08_Task01.txt'
with open(my_file, 'r') as my_text:
    my_lines = my_text.readlines()
    print('Number of lines is:', len(my_lines))
    line_count = 1
    for i in my_lines:
        print('Line number {} is containing {} words and {} symbols'.format(line_count, len(i.split()), len(i)))
        line_count += 1
