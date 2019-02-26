# Задача 7
# Пользователь вводит строку и символ.
# В строке найти все вхождения этого символа и перевести его в верхний регистр,
# а также удалить часть строки, начиная с последнего вхождения этого символа и до конца.


my_string = input('Enter string:')
my_sym = input('Enter symbol')
i = 0
while i < len(my_string):
    if my_string[i] == my_sym:
        string_new = my_string.replace(my_string[i], my_string[i].upper())
        i += 1
    else:
        i += 1
print(string_new)
