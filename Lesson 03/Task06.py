# Задача 5
# На вход поступают две строки. Необходимо выяснить, является ли вторая строка подстрокой первой.

str1 = input('Print the first string')
str2 = input('Print the second string')
if str1.find(str2) != -1:
    print('The second string is a part of the first one!')
else:
    print('No matches found!')
