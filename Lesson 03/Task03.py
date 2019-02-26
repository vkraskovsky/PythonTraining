# Задача 2
# Дана строка ‘Hello!Anthony!Have!A!Good!Day!’.
# Создать список, состоящий из отдельных слов [‘HELLO’, ‘ANTHONY’, ‘HAVE’, ‘A’, ‘GOOD’, ‘DAY’].

str_draft = 'Hello!Anthony!Have!A!Good!day'
list_final = str_draft.upper().split('!')
print(list_final)
