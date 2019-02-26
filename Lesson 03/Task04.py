# Задача 3
# Полученный список из задачи 2 вывести столбиком в отсортированном порядке.

str_draft = 'Hello!Anthony!Have!A!Good!day'
list_final = str_draft.upper().split('!')
list_sort = sorted(list_final)
for i in range(len(list_sort)):
    print(list_sort[i])
