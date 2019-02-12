# Задача 8
# Дан список кортежей grades = [(‘Ann’, 9), (‘John’, 7), (‘Smith’, 5), (‘George’, 6) ].
# Вывести информацию об оценках по возрастанию в виде:
# ‘Hello Ann! Your grade is 9’


grades = [('Ann', 9), ('John', 7), ('Smith', 5), ('George', 6)]


def select_second_element(a):
    return a[1]


sorted_grades = sorted(grades, key=select_second_element, reverse=True)
for i, j in sorted_grades:
    print('Hello', i, '! Your grade is ', j, '!')
