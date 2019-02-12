# Задача 2
# Найти и вывести все гласные буквы (без повторений),
# которые встречаются в самом коротком слове.
# Текст запрашивается у пользователя. Алфавит использовать любой.


my_string = input('Enter string:')
my_string_list = my_string.lower().split(sep='. ')
list_new = []
for i in my_string_list:
    list_new.extend(i.split(' '))
my_word = min(list_new, key=len)
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
print('Your vowels are:', set(my_word).intersection(vowels))
