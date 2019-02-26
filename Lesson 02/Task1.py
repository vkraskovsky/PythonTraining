# Запросить у пользователя строку слов, разделенных пробелами.
# Затем запросить разделитель, не являющийся буквой.
# Необходимо вывести исходную строку, в которой пробелы заменены введенным разделителем.

str1 = str(input('Enter string with spaces:'))
print('Your string is:', str1)
sep1 = str(input('Now enter separator:'))
print('Your separator is:', sep1, 'Replacing...')
str1 = str1.replace(' ', sep1)
print(str1)
